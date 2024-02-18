"""Mutating functions."""


__author__ = "730404818"


def manual_append(num1: list[int], num2: int) -> None:
    """Manual_append is a list and integer."""
    num1.append(num2)
    return None


def double(num: list[int]) -> None:
    """Double is a list that we are multiplying by 2."""
    index = 0
    while index < len(num):
        num[index] *= 2
        index += 1
    return None