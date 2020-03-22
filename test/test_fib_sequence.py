from .context import fib_sequence

import unittest


class FibonacciTestCases(unittest.TestCase):
    def test_fibonacci_base_case1(self):
        expected = 1
        actual = fib_sequence.fibonacci(1)
        failed_message = "fibonacci(n) did not compute the first Fibonacci number correctly."
        self.assertEqual(expected, actual, failed_message)

    def test_fibonacci_base_case2(self):
        expected = 1
        actual = fib_sequence.fibonacci(2)
        failed_message = "fibonacci(n) did not compute the second Fibonacci number correctly."
        self.assertEqual(expected, actual, failed_message)

    def test_fibonacci_lowest_edge_recur_case(self):
        expected = 2
        actual = fib_sequence.fibonacci(3)
        failed_message = "fibonacci(n) did not compute the third Fibonacci number correctly."
        self.assertEqual(expected, actual, failed_message)

    def test_fibonacci_second_lowest_edge_recur_case(self):
        expected = 3
        actual = fib_sequence.fibonacci(4)
        failed_message = "fibonacci(n) did not compute the fourth Fibonacci number correctly."
        self.assertEqual(expected, actual, failed_message)

    def test_fibonacci_bigger_recur_case(self):
        expected = 13
        actual = fib_sequence.fibonacci(7)
        failed_message = "fibonacci(n) did not compute the seventh Fibonacci number correctly."
        self.assertEqual(expected, actual, failed_message)


class FiboTopDownTestCases(unittest.TestCase):
    def test_fibo_top_down_base_case1(self):
        expected = 1
        actual = fib_sequence.fibo_top_down(1)
        failed_message = "fibo_top_down(n) did not compute the first Fibonacci number correctly."
        self.assertEqual(expected, actual, failed_message)

    def test_fibo_top_down_base_case2(self):
        expected = 1
        actual = fib_sequence.fibo_top_down(2)
        failed_message = "fibo_top_down(n) did not compute the second Fibonacci number correctly."
        self.assertEqual(expected, actual, failed_message)

    def test_fibo_top_down_lowest_edge_recur_case(self):
        expected = 2
        actual = fib_sequence.fibo_top_down(3)
        failed_message = "fibo_top_down(n) did not compute the third Fibonacci number correctly."
        self.assertEqual(expected, actual, failed_message)

    def test_fibo_top_down_second_lowest_edge_recur_case(self):
        expected = 3
        actual = fib_sequence.fibo_top_down(4)
        failed_message = "fibo_top_down(n) did not compute the fourth Fibonacci number correctly."
        self.assertEqual(expected, actual, failed_message)

    def test_fibo_top_down_bigger_recur_case(self):
        expected = 139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125
        actual = fib_sequence.fibo_top_down(500)
        failed_message = "fibo_top_down(n) did not compute the seventh Fibonacci number correctly."
        self.assertEqual(expected, actual, failed_message)


class FiboBottomUpTestCases(unittest.TestCase):
    def test_fibo_bottom_up_base_case1(self):
        fib_sequence.table = []
        expected = 1
        actual = fib_sequence.fibo_bottom_up(1)
        failed_message = "fibo_bottom_up(n) did not compute the first Fibonacci number correctly."
        self.assertEqual(expected, actual, failed_message)

    def test_fibo_bottom_up_base_case2(self):
        fib_sequence.table = []
        expected = 1
        actual = fib_sequence.fibo_bottom_up(2)
        failed_message = "fibo_bottom_up(n) did not compute the second Fibonacci number correctly."
        self.assertEqual(expected, actual, failed_message)

    def test_fibo_bottom_up_lowest_edge_recur_case(self):
        fib_sequence.table = []
        expected = 2
        actual = fib_sequence.fibo_bottom_up(3)
        failed_message = "fibo_bottom_up(n) did not compute the third Fibonacci number correctly."
        self.assertEqual(expected, actual, failed_message)

    def test_fibo_bottom_up_second_lowest_edge_recur_case(self):
        fib_sequence.table = []
        expected = 3
        actual = fib_sequence.fibo_bottom_up(4)
        failed_message = "fibo_bottom_up(n) did not compute the fourth Fibonacci number correctly."
        self.assertEqual(expected, actual, failed_message)

    def test_fibo_bottom_up_bigger_recur_case(self):
        fib_sequence.table = []
        expected = 139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125
        actual = fib_sequence.fibo_bottom_up(500)
        failed_message = "fibo_bottom_up(n) did not compute the seventh Fibonacci number correctly."
        self.assertEqual(expected, actual, failed_message)


if __name__ == '__main__':
    unittest.main()
