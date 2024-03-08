"""EX05- Dictionary Utility Function."""


__author__ = "730404818"


def invert(given_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values in the dictionary."""
    inverted_dict: dict[str, str] = {}
    for key in given_dict:
        if given_dict[key] in inverted_dict:
            raise KeyError("Duplicate value.")
        inverted_dict[given_dict[key]] = key
    return inverted_dict


def favorite_color(given_dict: dict[str, str]) -> str:
    """Returns the most popular color."""
    most_popular_color: str = ""
    max_count = 0
    for name in given_dict:
        color = given_dict[name]
        count: int = 0
        for other_name in given_dict:
            if given_dict[other_name] == color:
                count += 1
        if count > max_count or (count == max_count and most_popular_color is None):
            most_popular_color = color
            max_count = count
    return most_popular_color


def count(numbers: list[str]) -> dict[str, int]:
    """Counts the number of times each word appears."""
    result_dict: dict[str, int] = {}
    for item in numbers:
        if item in result_dict:
            result_dict[item] += 1
        else:
            result_dict[item] = 1
    return result_dict


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Alphabetizes the words."""
    result_dict: dict[str, list[str]] = {}
    for word in words:
        first_letter = word[0].lower()
        if first_letter not in result_dict:
            result_dict[first_letter] = []
        result_dict[first_letter].append(word)
    return result_dict


def update_attendance(students: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Gives a list of students in attendance each day."""
    if day in students: 
        students[day].append(student)
    else:
        students[day] = [student]
    return None 