import click

from sort_function import sort


@click.command()
@click.argument('width', type=click.FLOAT)
@click.argument('height', type=click.FLOAT)
@click.argument('length', type=click.FLOAT)
@click.argument('mass', type=click.FLOAT)
def sort_command(width: float, height: float, length: float, mass: float):
    try:
        classification = sort(width, height, length, mass)
        print(f"Classification is: {classification}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    sort_command()
