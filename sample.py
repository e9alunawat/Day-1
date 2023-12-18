"""Sum for the range 4212 to 18912513"""


def func(a, b):
    """Base Condition"""
    total = sum(range(a, b + 1))
    return total


if __name__ == "__main__":
    print(func(4212, 18912513))
