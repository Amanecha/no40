import click
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from dotenv import load_dotenv
import os

# .env ファイルの読み込み
load_dotenv()

# Azureリソースの認証とクライアント作成
def get_client():
    credential = AzureCliCredential()  # az loginでログイン済みのアカウントを使用
    subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID") # load_dotenv()で読み込んだ環境変数にアクセスして取得
    return ResourceManagementClient(credential, subscription_id) # Azureのリソース管理APIにアクセスするためのクライアント

# CLIとして複数コマンドをまとめるためのグループ定義
@click.group() 
def cli():
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

@cli.command(name='crg')
@click.argument('resource_group_name')
@click.option('--location', default='japaneast', help='Location of the resource group')
@click.option('-v', '--verbose', is_flag=True, help='Show details of the created resource group')
@click.option('-dr', '--dry-run', is_flag=True, help='Simulate the creation of the resource group')
def create_resource_group(resource_group_name, location, verbose, dry_run):
    """リソースグループを作成"""
    client = get_client()
    resource_group = client.resource_groups.create_or_update(
        resource_group_name, {'location': location}
    )
    click.echo(f"Resource group {resource_group.name} created in {resource_group.location}")
    if verbose:
        details = client.resource_groups.get(resource_group_name)
        click.echo("Resource Group Details:")
        click.echo(f"Name: {details.name}")
        click.echo(f"Location: {details.location}")
        click.echo(f"Provisioning State: {details.properties.provisioning_state}")
    if dry_run:
        details = client.resource_groups.get(resource_group_name)
        click.echo(f"Simulating resource group creation:")
        click.echo(f"Name: {resource_group_name}")
        click.echo(f"Location: {location}")
        click.echo(f"tag: {resource_group.tags}")
        click.echo(f"properties: {resource_group.properties}")
        return
# スクリプトが直接実行された場合にcli() を呼び出す
if __name__ == "__main__":
    cli()
