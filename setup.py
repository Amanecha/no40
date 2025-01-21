from setuptools import setup, find_packages

setup(
    name='azure_resources_cli',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'click',
        'azure-identity',
        'azure-mgmt-resource',
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'azure_resources_cli=azure_resources_cli.azure_resources_cli:cli'
        ]
    },
)