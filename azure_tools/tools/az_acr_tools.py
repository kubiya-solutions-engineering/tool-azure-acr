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
                - *show-tags*. Show tags for a repository in an Azure Container Registry.
                - *untag*. Untag an image in an Azure Container Registry.
                - *update*. Update the attributes of a repository or image in an Azure Container
                  Registry.
                """),
            required=True),
    ],
)

tool_registry.register("Azure Container Repository", azure_acr_tool)
