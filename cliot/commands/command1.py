import click


@click.command()
@click.option('--name', prompt='Your name', help='The person to greet.')
def command(name):
    """A simple command that greets NAME."""
    click.echo(f"Hello, {name}!")
