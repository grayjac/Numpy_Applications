#!/usr/bin/env python3


# ME499-S20 Python Lab 6
# Programmer: Jacob Gray
# Last Edit: 5/22/2020


import numpy as np


def compute_inertia_matrix(array, mass=1):
    """

    :param array: An Nx3 Numpy array.
    :param mass: Number. Mass of the object being sampled from.
    :return: 3x3 Numpy array representing the inertia matrix.
    """

    term1 = sum(array[:, 1] ** 2 + array[:, 2] ** 2)
    term2 = -1 * sum(array[:, 0] * array[:, 1])
    term3 = -1 * sum(array[:, 0] * array[:, 2])
    term4 = sum(array[:, 0] ** 2 + array[:, 2] ** 2)
    term5 = -1 * sum(array[:, 1] * array[:, 2])
    term6 = sum(array[:, 0] ** 2 + array[:, 1] ** 2)

    inertia = mass * np.array([[term1, term2, term3], [term2, term4, term5], [term3, term5, term6]])

    return inertia


def sample_sphere_polar(N):
    """

    :param N: Number.
    :return: 
    """


if __name__ == '__main__':
    array = np.arange(6).reshape(-1, 3)
    print(compute_inertia_matrix(array))
