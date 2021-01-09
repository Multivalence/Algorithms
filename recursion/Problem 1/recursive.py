import random

def sum_digits(n : int) -> int:
    """
    Given a non-negative integer n, return the sum of its digits.

    Parameters
    ----------
    n : int
       number to return the sum of

    Returns
    -------
    int
       sum of numbers digits

    """

    if n == 0:
        return 0

    x = sum_digits(n // 10) + (n % 10)
    return(x)


if __name__ == '__main__':
    number = random.randint(1,10000)
    print(sum_digits(number))