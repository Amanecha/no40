import click
from no40.utils import get_client

@click.command(name='crg')
@click.argument('resource_group_name')
@click.option('--location', default='japaneast', help='Location of the resource group')
@click.option('--tags', type=str, help='Tags for the resource group in key=value format, separated by commas')
@click.option('-v', '--verbose', is_flag=True, help='Show details of the created resource group')
@click.option('-dr', '--dry-run', is_flag=True, help='Simulate the creation of the resource group')

def create_resource_group(resource_group_name, location, verbose, dry_run, tags):
    """リソースグループを作成"""
    tag_dict = {}
    if tags:
        try:
            tag_dict = dict(tag.split('=') for tag in tags.split(','))
        except ValueError:
            click.echo("Invalid format for tags. Use key=value pairs separated by commas.")
            return
    if dry_run:
        click.echo(f"Simulating resource group creation:")
        click.echo(f"Name: {resource_group_name}")
        click.echo(f"Location: {location}")
        click.echo(f"tag: {tag_dict}")
        return

    client = get_client()
    resource_group = client.resource_groups.create_or_update(
        resource_group_name, {'location': location, 'tags': tag_dict}
    )
    click.echo(f"Resource group {resource_group.name} created in {resource_group.location}")
    if verbose:
        details = client.resource_groups.get(resource_group_name)
        click.echo("Resource Group Details:")
        click.echo(f"Name: {details.name}")
        click.echo(f"Location: {details.location}")
        click.echo(f"Provisioning State: {details.properties.provisioning_state}")
