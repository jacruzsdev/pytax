# -*- coding: utf-8 -*-

"""Console script for pytax."""
import sys
import click
from pytax.pytax import calc_tax


@click.command()
@click.argument('price', type=float)
@click.argument('tax', type=float)
def main(price, tax):
    """Console script for pytax."""
    full_price = calc_tax(price, tax)
    click.echo(full_price)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
