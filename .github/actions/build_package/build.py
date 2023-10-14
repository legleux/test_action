#!/usr/bin/env python
import os
import sys


for k,v in os.environ.items():
    print(k,v)
print(os.environ['PKG'])
