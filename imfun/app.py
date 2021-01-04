#!/usr/bin/env python

import click

from .lib import img2cartoon


@click.command()
@click.option(
    '-i',
    '--in-img',
    type=click.Path(exists=True),
    required=True,
    help='Original image',
)
@click.option(
    '-o',
    '--out-img',
    type=click.Path(),
    required=True,
    help='Converted cartoon image',
)
def main(in_img: str, out_img: str) -> None:
    click.echo(f"Converting image '{click.format_filename(in_img)}'")
    img2cartoon(in_img, out_img)
    click.echo(f"Cartoon image saved as '{click.format_filename(out_img)}'")


if __name__ == '__main__':
    main()
