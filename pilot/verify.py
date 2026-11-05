import unittest

from normalize import normalize_counts


class NormalizeCountsTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(normalize_counts([]), {"count": 0, "total": 0, "maximum": 0})

    def test_zero(self):
        self.assertEqual(normalize_counts([0]), {"count": 1, "total": 0, "maximum": 0})

    def test_multiple_values(self):
        self.assertEqual(normalize_counts([2, 0, 7, 2]), {"count": 4, "total": 11, "maximum": 7})

    def test_invalid_elements(self):
        class IntSubclass(int):
            pass

        for value in (True, False, 1.0, "1", IntSubclass(1)):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    normalize_counts([value])

    def test_negative(self):
        with self.assertRaises(ValueError):
            normalize_counts([0, -1, 2])

    def test_non_list(self):
        for value in (None, (), (1, 2), "12", 1, {1: 2}):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    normalize_counts(value)

    def test_input_unchanged(self):
        values = [3, 0, 1]
        normalize_counts(values)
        self.assertEqual(values, [3, 0, 1])

    def test_distinct_dictionaries(self):
        values = [2]
        first = normalize_counts(values)
        second = normalize_counts(values)
        self.assertIsNot(first, second)
        first["total"] = 99
        self.assertEqual(second, {"count": 1, "total": 2, "maximum": 2})


if __name__ == "__main__":
    unittest.main()
