def factorial(n):
    """
    Recursive Function to calculate the factorial of a number
    :param n: integer
    :return: factorial
    """
    if n <= 1:
        return 1
    return n * factorial(n - 1)
