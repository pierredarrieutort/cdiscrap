# cdiscount price parser

## Installation
```powershell
# From Pypi
$ pip install cdiscountpriceparser

# Locally
$ pip install -e .
```

## Usage
```python
python

>>> from cdiscount_parser.price_parser import parse_price

# Return "False"
>>> parse_price()

# Return "False"
>>> parse_price("random")

# Return "1776.6"
>>> parse_price("del5397184246030")
```

## Development
```powershell
$ pip install -e .[dev]
```

## Docker usage
```powershell
$ docker build --tag price_parser .
$ docker run --name price_parser -p 5000:5000 price_parser
```
