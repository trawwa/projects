#!/usr/bin/env python3

"""Simple fizzbuzz generator.

This script prints out a sequence of numbers from a provided range
with the following restrictions:

- if the number is divisible by 3, then print out "fizz",
- if the number is divisible by 5, then print out "buzz",
- if the number is divisible by 3 and 5, then print out "fizzbuzz".
"""

import sys
for n in range(int(sys.argv[1]), int(sys.argv[2])):
    if n % 3 == 0 and n % 5 == 0:
        print("fizzbuzz")
    elif n % 3 == 0:
        print("fizz")
    elif n % 5 == 0:
        print("buzz")
    else:
        print(n)
