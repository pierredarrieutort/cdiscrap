# Cdiscount price parser

Python package capable of raising the price of any product on the site www.cdiscount.com

## Table of contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Development](#development)
4. [Flask](#flask)
5. [Docker usage](#docker-usage)
6. [Collaborators](#collaborators)

## Installation
```powershell
# From Pypi
$ pip install cdiscountpriceparser

# Locally
$ cd cdiscount
$ pip install -e .
```
[Link to package on Pypi](https://pypi.org/project/cdiscountpriceparser/)

## Usage
```python
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
$ cd cdiscount
$ pip install -e .[dev]
```

## Flask
```powershell
$ cd www
$ flask run
```

## Docker usage
```powershell
$ docker build --tag price_parser .
$ docker run --name price_parser -p 5000:5000 price_parser
```

## Collaborators
<table>
    <tbody>
        <tr>
            <td align="center" width="140">
                <a href="https://github.com/pierredarrieutort">
                    <img src="https://avatars0.githubusercontent.com/u/25182438?s=460&amp;v=4" alt="Pierre Darrieutort" width="100px;" />
                    <br />
                    <sub><strong>Pierre Darrieutort</strong></sub>
                </a>
            </td>
            <td align="center" width="140">
                <a href="https://github.com/mathieudaix">
                    <img src="https://scontent.xx.fbcdn.net/v/t1.15752-9/95019821_1336186823257776_6091369584101687296_n.jpg?_nc_cat=109&_nc_sid=b96e70&_nc_ohc=vzl7zKAyKi0AX9JY36K&_nc_ad=z-m&_nc_cid=0&_nc_zor=9&_nc_ht=scontent.xx&oh=c0b399312a81efd43099d87ea03d8b37&oe=5ECFC9AF" alt="Mathieu Daix" width="100px;" />
                    <br />
                    <sub><strong>Mathieu Daix</strong></sub>
                </a>
            </td>
        </tr>
    </tbody>
</table>
