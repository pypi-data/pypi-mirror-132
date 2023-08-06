# recast
python bit recaster

Convenient functions for converting bytes into various different python
types. These functions do not modify the underlying bits, but rather,
how they are interpreted in python.

## Examples
```py
>>> import recast

>>> hex(recast.int2uint(-1))
'0xffffffff'

>>> recast.double2bytes(4.400150012111731e-110)
b'recast:)'
```

## License
recast - python bit recaster
Copyright (C) 2021 Phil Dreizen and Miccah Castorina
This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
USA
