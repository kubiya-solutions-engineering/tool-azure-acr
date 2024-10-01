from setuptools import setup, find_packages

setup(
    name="tool-azure-acr",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "kubiya-sdk",
    ],
)
