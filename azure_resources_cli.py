import click
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from dotenv import load_dotenv
import os

# .env ファイルの読み込み
load_dotenv()

# Azureリソースの認証とクライアント作成
def get_client():
    credential = AzureCliCredential()  # Azure CLIでログイン済みのアカウントを使用
    subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID") # サブスクリプションIDを設定
    return ResourceManagementClient(credential, subscription_id)

@click.group()
def cli():
    """Azureリソースを操作するCLIツール"""
    pass

@cli.command()
def list_resource_groups():
    """リソースグループ一覧を取得"""
    client = get_client()
    for rg in client.resource_groups.list():
        click.echo(f"Name: {rg.name}, Location: {rg.location}")

@cli.command()
@click.argument('resource_group_name')
def list_resources(resource_group_name):
    """指定されたリソースグループ内のリソースを一覧表示"""
    client = get_client()
    resources = client.resources.list_by_resource_group(resource_group_name)
    for resource in resources:
        click.echo(f"Name: {resource.name}, Type: {resource.type}, Location: {resource.location}")

if __name__ == "__main__":
    cli()
