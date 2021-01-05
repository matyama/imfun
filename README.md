![ImFun](https://github.com/matyama/imfun/workflows/ImFun/badge.svg) [![PyPI version](https://badge.fury.io/py/imfun.svg)](https://badge.fury.io/py/imfun) [![PyPI status](https://img.shields.io/pypi/status/imfun.svg)](https://pypi.python.org/pypi/imfun/) [![PyPI pyversions](https://img.shields.io/pypi/pyversions/imfun.svg)](https://pypi.python.org/pypi/imfun/)

# ImFun
Convert an image to cartoon!

## Installation
This application (package) is available on *PyPI*, so it can be installed using `pip` or `pipx`.
```
$ pipx install imfun
  installed package imfun 0.1.0, Python 3.8.5
  These apps are now globally available
    - imfun
done! ✨ 🌟 ✨
```

## Usage
One can run the `imfun` app to convert an image to a cartoon like this
```
$ imfun -i examples/prague-castle.jpg -o examples/prague-castle-cartoon.jpg
Converting image 'examples/prague-castle.jpg'
Cartoon image saved as 'examples/prague-castle-cartoon.jpg'
```
assuming that `examples/prague-castle.jpg` exists - or try it on any other image ;)

## Examples
<img src="./examples/prague.jpg" alt="Prague castle (original)" title="Original Image" width="250">
<img src="./examples/prague-cartoon.jpg" alt="Prague castle (cartoon)" title="Cartoon Image" width="250">

## Development
Development setup requires [Poetry](https://python-poetry.org/) to be installed.
Once the repository is cloned, one can setup everything with
```bash
make setup
```
