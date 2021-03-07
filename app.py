#!/usr/bin/env python
import click
import random

@click.command()
@click.option("--minval")
@click.option("--maxval")
def hello(minval, maxval):
    click.echo(f'Hello User!')
    click.echo(f'The minimum value is {minval}')
    click.echo(f'The maximum value is {maxval}')
    click.echo(f'************************')
    click.echo(f'ROLLING THE DICE')
    click.echo(f'************************')
    val = random.randint(int(minval), int(maxval))
    click.echo(f'The Result is {val}')

if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    hello()