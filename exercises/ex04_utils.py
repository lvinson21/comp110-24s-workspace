"""Lists Excersize Four."""


__author__ = "730404818"


def all(my_list: list[int], num: int) -> bool:
    for elem in my_list:
        if elem != num:
            return False
    return True


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max_value = input[0]
    for nums in input:
        if nums > max_value:
            max_value = nums
    return max_value


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    if len(list_one) != len(list_two):
        return False
    
    index = 0

    while index < len(list_one):
        if list_one[index] != list_two[index]:
            return False
        index += 1
    
    return True


def extend(list_one: list[int], list_two: list[int]) -> None:
    index = 0
    while index < len(list_two):
        list_one.append(list_two[index])
        index += 1
