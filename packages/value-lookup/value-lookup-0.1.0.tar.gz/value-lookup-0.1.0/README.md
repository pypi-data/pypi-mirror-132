Value lookup in an array Python Library
===========================

Python library to search value into inside array. This doesn't cover object analysis.

[![Coverage Status](https://coveralls.io/repos/daviddrysdale/python-phonenumbers/badge.svg?branch=dev&service=github)](https://github.com/eudagraca/value-lookuphe)

Motivation
------------
Value lookup help the way we can search for a value within a list


Installation
------------

Install using [pip](https://pypi.org/project/value-lookup/) with:
```
pip install value-lookup
```

Example Usage
-------------

```
from  value_lookup import vlookup

#### Test 1
test1 = vlookup(1, [1,2,3,4,5,6], True)
print(test1)
```

### Output:
    {'founded_values': ['1'], 'size_of_returned_list': 1, 'object_type': <class 'list'>}

#### Test 2

```
test2 = vlookup(1, [1,2,3,4,5,6])
print(test2)
```
### Output:
```
    True
```

#### Author

Euclídio Venâncio • euclidiodagracavenancio@gmail.com
