import unittest

from solutions.t001_merge_and_sort_intervals import merge_high_definition_intervals


class Test001MergeAndSortIntervals(unittest.TestCase):
    def test_handle_example_case(self):
        _input = [[1, 3], [2, 6], [8, 10], [15, 18]]
        result = merge_high_definition_intervals(_input)
        self.assertEqual([[1, 6], [8, 10], [15, 18]], result)

    def test_handle_completely_included_case(self):
        _input = [[1, 10], [2, 6], [8, 10], [15, 18]]
        result = merge_high_definition_intervals(_input)
        self.assertEqual([[1, 10], [15, 18]], result)

    def test_handle_unordered_case(self):
        _input = [[15, 18], [1, 10], [8, 10], [2, 6]]
        result = merge_high_definition_intervals(_input)
        self.assertEqual([[1, 10], [15, 18]], result)

    def test_handle_touching_case(self):
        _input = [[1, 2], [2, 3], [3, 4], [5, 6]]
        result = merge_high_definition_intervals(_input)
        self.assertEqual([[1, 4], [5, 6]], result)
