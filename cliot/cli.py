import click
from cliot.commands import command1, command2


@click.group()
def cli():
    """Main entry point for the CLI."""
    pass


cli.add_command(command1.command)
cli.add_command(command2.command)

if __name__ == "__main__":
    cli()
