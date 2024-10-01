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
                The Azure CLI command to run (example: account). Do not add `az acr` at the front.
                Note that the valid commands are:
                - *repository delete*. Delete a repository or image in an Azure Container 
                  Registry.
                - *repository list*. List repositories in an Azure Container Registry.
                - *repository show*. Get the attributes of a repository or image in an Azure
                  Container Registry.
                - *repository show-tags*. Show tags for a repository in an Azure Container Registry.
                - *repository untag*. Untag an image in an Azure Container Registry.
                - *repository update*. Update the attributes of a repository or image in an Azure
                  Container Registry.
                """),
            required=True),
    ],
)

tool_registry.register("Azure Container Repository", azure_acr_tool)
