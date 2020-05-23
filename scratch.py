#!/usr/bin/env python3


# ME499-S20 Python Lab 6
# Programmer: Jacob Gray
# Last Edit: 5/22/2020


import numpy as np

array = np.arange(6).reshape(2, 3)

print(array)
print(sum(array[:, 1] ** 2 + array[:, 2] ** 2))
