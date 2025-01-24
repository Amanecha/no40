import click
from no40.commands.create_resource_group import create_resource_group
from no40.commands.list_resource_groups import list_resource_groups
from no40.commands.list_resources import list_resources

# CLIとして複数コマンドをまとめるためのグループ定義
@click.group()
def cli():
    pass

cli.add_command(create_resource_group)
cli.add_command(list_resource_groups)
cli.add_command(list_resources)

# スクリプトが直接実行された場合にcli() を呼び出す
if __name__ == "__main__":
    cli()
