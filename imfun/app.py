#!/usr/bin/env python

import click
import cv2

from .lib import (
    BLUR_VALUE,
    COLORS,
    FILTER_DIAMETER,
    LINE_SIZE,
    SIGMA_COLOR,
    SIGMA_SPACE,
    convert,
)


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
@click.option(
    '-l',
    '--line',
    type=click.IntRange(1, 16, clamp=True),
    default=LINE_SIZE,
    help='Line size in the cartoon',
)
@click.option(
    '-b',
    '--blur',
    type=click.IntRange(0, 10, clamp=True),
    default=BLUR_VALUE,
    help='Blur value to use for the cartoon',
)
@click.option(
    '-c',
    '--colors',
    type=click.IntRange(4, 16, clamp=True),
    default=COLORS,
    help='Number of colors in the cartoon',
)
@click.option(
    '-fd',
    '--filter-diameter',
    type=click.IntRange(2, 10, clamp=True),
    default=FILTER_DIAMETER,
    help='Diameter of pixel neghborhood for filtering',
)
@click.option(
    '-sc',
    '--sigma-color',
    type=click.IntRange(10, 300, clamp=True),
    default=SIGMA_COLOR,
    help='Filter parameter determining areas of semi-equal color',
)
@click.option(
    '-ss',
    '--sigma-space',
    type=click.IntRange(10, 300, clamp=True),
    default=SIGMA_SPACE,
    help='Filter parameter determinig how far can pixels influence each other '
    'as long as their color is similar',
)
def main(
    in_img: str,
    out_img: str,
    line: int,
    blur: int,
    colors: int,
    filter_diameter: int,
    sigma_color: int,
    sigma_space: int,
) -> None:
    click.echo(f"Converting image '{click.format_filename(in_img)}'")
    img = cv2.imread(in_img)

    cartoon_img = convert(
        img,
        line_size=line,
        blur_value=blur,
        colors=colors,
        filter_diameter=filter_diameter,
        sigma_color=sigma_color,
        sigma_space=sigma_space,
    )

    cv2.imwrite(out_img, cartoon_img)
    click.echo(f"Cartoon image saved as '{click.format_filename(out_img)}'")


if __name__ == '__main__':
    main()
