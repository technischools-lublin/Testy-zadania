import unittest
from src.zadanie1 import sum_numbers_from_file

class TestSumNumbers(unittest.TestCase):
    def test_sum_numbers_from_file_empty_file(self):
        # GIVEN
        file_path = "./src/empty_file.txt"
        expected_sum = 0

        # WHEN
        result = sum_numbers_from_file(file_path)

        # THEN
        self.assertEqual(result, expected_sum)

    def test_sum_numbers_from_file_valid_numbers(self):
        # GIVEN
        file_path = "./src/file.txt"
        expected_sum = 6

        # WHEN
        result = sum_numbers_from_file(file_path)

        # THEN
        self.assertEqual(result, expected_sum)

    def test_sum_numbers_from_file_invalid_values(self):
        # GIVEN
        file_path = "./src/invalid_values_file.txt"
        expected_error_message = "Invalid value found in the file."

        # WHEN
        with self.assertRaises(ValueError) as context:
            sum_numbers_from_file(file_path)

        # THEN
        self.assertTrue(expected_error_message in str(context.exception))

    def test_sum_numbers_from_file_number_out_of_range(self):
        # GIVEN
        file_path = "./src/out_of_range_file.txt"
        expected_error_message = "Number out of range."

        # WHEN
        with self.assertRaises(ValueError) as context:
            sum_numbers_from_file(file_path)

        # THEN
        self.assertTrue(expected_error_message in str(context.exception))

    def test_sum_numbers_from_file_invalid_file_path(self):
        # GIVEN
        file_path = "./nonexistent_file.txt"
        expected_error_message = "File not found."

        # WHEN
        with self.assertRaises(FileNotFoundError) as context:
            sum_numbers_from_file(file_path)

        # THEN
        self.assertTrue(expected_error_message in str(context.exception))
