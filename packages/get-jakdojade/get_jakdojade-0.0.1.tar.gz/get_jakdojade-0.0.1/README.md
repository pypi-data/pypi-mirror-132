# GET_jakdojade

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Wheel Status](https://img.shields.io/pypi/wheel/get-jakdojade)](https://pypi.python.org/pypi/get-jakdojade/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/get-jakdojade)](https://pypi.python.org/pypi/get-jakdojade/)
[![PyPI - Status](https://img.shields.io/pypi/status/get-jakdojade)](https://pypi.python.org/pypi/get-jakdojade/)
[![Latest version](https://img.shields.io/pypi/v/get-jakdojade)](https://pypi.python.org/pypi/get-jakdojade/)

Jakdojade URL generator

Based on [jakdojade documentation](https://jakdojade.pl/public/pages/api/http_get.html)

## Usage

```python
import datetime

from get_jakdojade import generate

print(generate(
    city='warszawa',
    from_name='Your home',
    from_coordinate_latitude='52.275222',
    from_coordinate_longitude='20.914578',
    to_name='My shop',
    to_coordinate_latitude='52.211184',
    to_coordinate_longitude='20.984775',
    date_time=datetime.datetime(2021, 12, 28, 9, 00),
    is_arrival=True,
))
```

## Release

1. Change version in setup.py to `x.y.z.dev0` (or leave if minor version bump) and ensure changelog is up to date.
   (`Nothing changed yet.` is not ok, CI will fail)
2. Tag head of master branch with `x.y.z` without `.dev0`

**Important**: release ALWAYS is from master branch! So keep master untouched when you want to release.
