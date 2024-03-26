from parameterized import parameterized
import unittest

from cornsnake import util_file


class TestUtilFile(unittest.TestCase):
    @parameterized.expand(
        [
            ("C:\\temp\\x.txt", "C:\\temp", True),
            ("C:\\temp\\x.txt", "C:\\temp\\", True),
            ("C:\\temp\\d1\\d2\\x.txt", "C:\\temp\\", True),
            ("C:\\temp\\d1\\d2\\x.txt", "C:\\temp\\d1", True),
            ("C:\\temp\\d1\\d2\\x.txt", "C:\\temp\\d1\\", True),
            ("C:\\temp\\d1\\d2\\x.txt", "C:\\temp\\d1\\d2", True),
            ("C:\\temp\\d1\\d2\\x.txt", "C:\\temp\\d1\\d2\\", True),
            ("C:\\temp2\\x.txt", "C:\\temp\\", False),
            ("C:\\temp\\d1\\d2\\x.txt", "C:\\temp\\d1\\d3", False),
        ]
    )
    def test_is_file_under_dir(self, file_path, dir_path, expected):
        # Arrange

        # Act
        actual = util_file.is_file_under_dir(file_path, dir_path)

        # Assert
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
