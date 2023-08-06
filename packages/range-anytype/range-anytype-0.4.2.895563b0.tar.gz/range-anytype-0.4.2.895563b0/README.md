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
