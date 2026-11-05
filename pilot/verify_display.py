"""Executable unittest coverage for display_counts."""

import sys
import unittest

sys.dont_write_bytecode = True

if __package__:
    from .display import display_counts
else:
    from display import display_counts


class DisplayCountsTests(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(display_counts([]), "count=0; total=0; maximum=0")

    def test_zero_values(self):
        self.assertEqual(display_counts([0, 0]), "count=2; total=0; maximum=0")

    def test_multiple_integers_and_exact_format(self):
        self.assertEqual(display_counts([3, 12, 5]), "count=3; total=20; maximum=12")

    def test_rejects_bool(self):
        for value in (True, False):
            with self.subTest(value=value), self.assertRaises(TypeError):
                display_counts([value])

    def test_rejects_float(self):
        with self.assertRaises(TypeError):
            display_counts([1.0])

    def test_rejects_non_list(self):
        for values in (None, (), (1, 2), "12", {1, 2}, {"count": 1}, 1):
            with self.subTest(values=values), self.assertRaises(TypeError):
                display_counts(values)

    def test_rejects_negative(self):
        with self.assertRaises(ValueError):
            display_counts([2, -1])

    def test_input_unchanged(self):
        for values in ([5, 0, 2, 5], [1, -1], [1, True], [1, 2.0]):
            original = values.copy()
            with self.subTest(values=values):
                if any(type(value) is not int for value in values):
                    with self.assertRaises(TypeError):
                        display_counts(values)
                elif any(value < 0 for value in values):
                    with self.assertRaises(ValueError):
                        display_counts(values)
                else:
                    display_counts(values)
                self.assertEqual(values, original)
                self.assertEqual(list(map(type, values)), list(map(type, original)))


if __name__ == "__main__":
    unittest.main()
