import os

import cv2
import py.path  # pylint: disable=no-name-in-module,import-error
import pytest
from click.testing import CliRunner

from imfun.app import main

img_dir = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    os.pardir,
    'examples',
)


@pytest.fixture(scope='module')
def runner() -> CliRunner:
    return CliRunner()


# pylint: disable=no-member,redefined-outer-name
def test_app_sanity(tmpdir: py.path.local, runner: CliRunner) -> None:
    in_img = os.path.join(img_dir, 'prague.jpg')
    in_shape = cv2.imread(in_img).shape

    out_dir = tmpdir.mkdir('imfun')
    out_img = os.path.join(out_dir, 'prague-cartoon.jpg')

    result = runner.invoke(main, args=['-i', in_img, '-o', out_img])

    if result.exit_code != 0:
        raise result.exception

    assert out_dir.listdir('*.jpg') != []

    out_shape = cv2.imread(out_img).shape
    assert in_shape == out_shape


# pylint: disable=no-member,redefined-outer-name
def test_img_not_exists(tmpdir: py.path.local, runner: CliRunner) -> None:
    in_img = os.path.join(img_dir, 'missing.jpg')

    out_dir = tmpdir.mkdir('imfun')
    out_img = os.path.join(out_dir, 'cartoon.jpg')

    result = runner.invoke(main, args=['-i', in_img, '-o', out_img])
    assert result.exit_code != 0
