# range-anytype

## Usage

This package is using for Range object for any type.

## How to use it

import it by: `from range_anytype import Range, ProtectedRange`. No any additional modules or packages will be installed. If you cannot install it by pip, please download the source and extract it into sys.path.

To see examples, please visit example.py, or type `from range_anytype import example`.

## Range

Create a range for any type that supports addition calculation.

## ProtectedRange

Create a range for any type that supports addition and subtraction calculation. This can protect program because it detects the supporting of subtraction of the type. Some types like `str`, `list`, `tuple`, only support addition, not support subtraction.

## Cautions

If you are using Python 2.1 or lower, it will import from py1compa.py (means "Python 1's compatible"). If you want to iter the object, please define these functions if the Python version does not have `iter` or `next` function:
```python3
iter = lambda obj: obj.__iter__()
next = lambda obj: obj.next()
```

If you are using a long-filename-less supported Microsoft OS(e.g. MS-DOS 5.0), please change the directory name from "range_anytype" to "rangeant".
