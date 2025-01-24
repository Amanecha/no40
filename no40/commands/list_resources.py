import click
from no40.utils import get_client

@click.command()
@click.argument('resource_group_name')
def list_resources(resource_group_name):
    """指定されたリソースグループ内のリソースを一覧表示"""
    client = get_client()
    resources = client.resources.list_by_resource_group(resource_group_name)
    for resource in resources:
        click.echo(f"Name: {resource.name}, Type: {resource.type}, Location: {resource.location}")
