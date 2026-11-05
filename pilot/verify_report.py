import unittest

from report import report_counts


class ReportCountsTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(report_counts([]), '{"count":0,"maximum":0,"total":0}')

    def test_multiple_integers_and_exact_format(self):
        self.assertEqual(
            report_counts([2, 0, 7, 2]),
            '{"count":4,"maximum":7,"total":11}',
        )

    def test_invalid_elements(self):
        class IntSubclass(int):
            pass

        for value in (True, False, 1.0, "1", None, IntSubclass(1)):
            with self.subTest(value=value):
                with self.assertRaisesRegex(TypeError, "^values must contain built-in integers$"):
                    report_counts([value])

    def test_invalid_containers(self):
        for value in (None, (), (1, 2), "12", 1, True, {1: 2}):
            with self.subTest(value=value):
                with self.assertRaisesRegex(TypeError, "^values must be a list$"):
                    report_counts(value)

    def test_negative(self):
        with self.assertRaisesRegex(ValueError, "^values must be nonnegative$"):
            report_counts([0, -1, 2])

    def test_input_unchanged(self):
        for values in ([3, 0, 1], [0, -1, 2], [1, True]):
            original = values.copy()
            with self.subTest(values=values):
                if any(type(value) is not int for value in values):
                    with self.assertRaises(TypeError):
                        report_counts(values)
                elif any(value < 0 for value in values):
                    with self.assertRaises(ValueError):
                        report_counts(values)
                else:
                    report_counts(values)
                self.assertEqual(values, original)


if __name__ == "__main__":
    unittest.main()
