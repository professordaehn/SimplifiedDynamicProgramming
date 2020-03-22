"""
The Fibonacci sequence is the sequence 1, 1, 2, 3, 5, 8, 13, ...
Formally, the ith Fibonacci number is given by Fi = F(i-1) + F(i-2)
with F1 = F2 = 1.
"""


def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number using naive recursive implementation.
    :param n: the index into the sequence
    :return: The nth Fibonacci number is returned.
    """
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


d = {}  # Dictionary for table to store values


def fibo_top_down(n: int) -> int:
    """
    Calculate the nth Fibonacci number using a top-down, dynamic programming approach.
    :param n: the index into the sequence
    :return: The nth Fibonacci number is returned.
    """
    if n == 1 or n == 2:
        return 1
    if d.get(n, None) is None:  # if value is not stored
        d[n] = fibo_top_down(n - 1) + fibo_top_down(n - 2)  # store it
    return d[n]


table = []  # List/array for table to store results


def fibo_bottom_up(n: int) -> int:
    """
    Calculate the nth Fibonacci number using a bottom-up, dynamic programming approach.
    :param n: the index into the sequence
    :return: The nth Fibonacci number is returned.
    """
    table.append(1)
    table.append(1)
    for i in range(2, n):
        table.append(table[i - 1] + table[i - 2])
    return table[n - 1]
