#!/usr/bin/env python

import click
import cv2

from imfun import convert


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
def cartoon(in_img: str, out_img: str) -> None:

    click.echo(f"Converting image '{click.format_filename(in_img)}'")
    img = cv2.imread(in_img)

    cartoon_img = convert(img)

    cv2.imwrite(out_img, cartoon_img)
    click.echo(f"Resulting image saved as '{click.format_filename(out_img)}'")


if __name__ == '__main__':
    cartoon()
