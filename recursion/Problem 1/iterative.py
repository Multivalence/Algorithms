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

    sum = 0
    for i in [int(i) for i in str(n)]:
        sum += i

    return sum


if __name__ == '__main__':
    number = random.randint(1,10000)
    print(sum_digits(number))