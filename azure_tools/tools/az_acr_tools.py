from kubiya_sdk.tools import Arg
from .base import AzureACRCliTool
from kubiya_sdk.tools.registry import tool_registry
from datetime import datetime, timedelta

azure_acr_tool = AzureACRCliTool(
    name="azure_acr_cli",
    description=(
        "Logs in to Azure CLI and then runs the specified Azure Container Repository command."
        ),
    content="az acr repository {{ .command}}",
    args=[
        Arg(name="command",
            type="str",
            description=("""
                The Azure CLI command to run (example: account). Do not add `az acr repository` at
                the front. Note that the valid commands are:
                - *delete*. Delete a repository or image in an Azure Container Registry.
                - *list*. List repositories in an Azure Container Registry.
                - *show*. Get the attributes of a repository or image in an Azure Container
                  Registry.
                - *untag*. Untag an image in an Azure Container Registry.
                - *update*. Update the attributes of a repository or image in an Azure Container
                  Registry.
                """),
            required=True),
    ],
)

list_tags = AzureACRCliTool(
    name="list_tags",
    description=("""
        Shows tags of a provided Azure ACR registry and repository. Optionally, a number of days
        describing how old a tag is, and/or what the tags starts with may also be passed as
        arguments.
        """),
    content="""
            export NEW_DATE=$(date -d "{{ .num_days}} days ago" +%Y-%m-%d)
            az acr repository show-tags -n {{ .registry}} --repository {{ .repository}} --detail \
            --query "[?lastUpdateTime<'$NEW_DATE' && starts_with(name, '{{ .starts_with}}')].{Name:name, LastUpdate:lastUpdateTime}" 
            """,
    args=[
        Arg(name="registry", 
            type="str", 
            description=("The Azure ACR registry."), 
            required=True),
        Arg(name="repository",  
            type="str", 
            description=("The Azure ACR repository within the chosen registry."), 
            required=True),
        Arg(name="num_days",
            type="str",
            description=("The number of days indicating age of tags. For example, `today` would be `0` and `two days ago` would be `2`."),
            default="0"
            required=True),
        Arg(name="starts_with",
            type="str",
            description=("A string to filter tags that start with this value. Use the default value is an empty string if not given one."),
            default="",
            required=True),
    ],
)

#azure_delete_tags_older_than_date = AzureACRCliTool(
#    name="azure_delete_tags_older_than_date",
#    description=("Deletes tags of a provided Azure ACR registry and repository that are older than a specified date."),
#    content="""
#            export NEW_DATE=$(date -d "{{ .num_days}} days ago" +%Y-%m-%d)
#            for tag in $(az acr repository show-tags -n {{ .registry}} --repository {{ .repository}} --query "[?lastUpdateTime<'$NEW_DATE' && starts_with(@, '{{ .filter }}')].name" -o tsv); do
#                az acr repository delete -n {{ .registry}} --image {{ .repository }}:$tag --yes
#            done
#            """,
#    args=[
#        Arg(name="registry", 
#            type="str", 
#            description=("The Azure ACR registry."), 
#            required=True),
#        Arg(name="repository",  
#            type="str", 
#            description=("The Azure ACR repository within the chosen registry."), 
#            required=True),
#        Arg(name="filter",
#            type="str",
#            description=("A string to filter tags that start with this value."),
#            required=False),
#        Arg(name="num_days",
#            type="int",
#            description=("The number of days indicating age of tags. For example, `today` would be `0` and `two days ago` would be `2`."),
#            required=True),
#    ],
#)


tool_registry.register("Azure Container Repository", list_tags)
tool_registry.register("Azure Container Repository", azure_acr_tool)
#tool_registry.register("Azure Container Repository", azure_delete_tags_older_than_date)
