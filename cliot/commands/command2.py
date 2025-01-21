import click


@click.command()
@click.option("--count", default=1, help="Number of greetings.")
def command(count):
    """A command that prints a greeting multiple times."""
    for _ in range(count):
        click.echo("Hello!")
