from kubiya_sdk.tools import Arg
from .base import AzureACRCliTool
from kubiya_sdk.tools.registry import tool_registry

azure_acr_tool = AzureACRCliTool(
    name="azure_acr_cli",
    description=(
        "Logs in to Azure CLI and then runs the specified Azure Container Repository command."
        ),
    content="{{ .command}}",
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

azure_show_tags_older_than_date = AzureACRCliTool(
    name="azure_show_tags_older_than_date",
    description=("""
        Shows tags of a provided Azure ACR registry and repository that are older than a specified
        date."
        """),
    content="""show-tags -n {{ .registry}} --repository {{ .repository}} --detail \
            --query "[?lastUpdateTime<'2024-09-02'].{Name:name, LastUpdate:lastUpdateTime}" \
            --orderby time_asc --top 10""",
    args=[
        Arg(name="registry", 
            type="str", 
            description=("The Azure ACR registry."), 
            required=True),
        Arg(name="repository",  
            type="str", 
            description=("The Azure ACR repository within the chosen registry."), 
            required=True),
        Arg(name="date",
            type="str",
            description=("A date in the format `YYYY-MM-DD` to filter tags."),
            required=True),
    ],
)

tool_registry.register("Azure Container Repository", azure_show_tags_older_than_date)
tool_registry.register("Azure Container Repository", azure_acr_tool)
