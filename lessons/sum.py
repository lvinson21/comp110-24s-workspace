"""Summing the elements of a list using different loops."""


__author__ = "730404818"


def w_sum(vals: list[float]) -> float:
    """Adds all the floats in the list together."""
    idx = 0
    total_value = 0.0
    while idx < len(vals):
        total_value += vals[idx]
        idx += 1
    return total_value


def f_sum(vals: list[float]) -> float:
    """Adds totals using a for and in loop."""
    total = 0.0
    for nums in vals:
        total += nums
    return total


def f_range_sum(vals: list[float]) -> float:
    """Adds totals using range."""
    total = 0.0
    for idx in range(0, len(vals)):
        total += vals[idx]
    return total
