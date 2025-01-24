import click
from no40.utils import get_client

@click.command()
def list_resource_groups():
    """リソースグループ一覧を取得"""
    client = get_client()
    for rg in client.resource_groups.list():
        click.echo(f"Name: {rg.name}, Location: {rg.location}")
