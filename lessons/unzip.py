"""Splitting a dictionary into two lists."""


__author__ = "730404818"


def get_keys(dictionary: dict[str, int]) -> list[str]:
    """Returning the key values in a list."""
    if not dictionary:
        return []
    key_list: list[str] = []
    for key in dictionary:
        key_list.append(key)
    return key_list


def get_values(dictionary: dict[str, int]) -> list[int]:
    """Returning the values in a list."""
    if not dictionary:
        return []
    values_list: list[int] = []
    for values in dictionary:
        values_list.append(dictionary[values])
    return values_list