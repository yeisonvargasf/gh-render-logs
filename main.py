import click

@click.command()
def hello():
    click.secho('Hello World without whitespace', fg='green')
    click.secho('  Hello World with styled whitespace', fg='green');
    click.echo('  ' + click.style('Hello World with non-styled whitespace', fg='green'))


if __name__ == '__main__':
    hello()

