# cdiscount price parser

## Installation
```python
pip install cdiscountpriceparser
```

## Usage
```python
python
from price_parser import parse_price

# Generate "Cet id n'est pas référencé."
parse_price()

# Generate "1776.6"
parse_price("del5397184246030")
```

## Development
```python
pip install -e .[dev]
```