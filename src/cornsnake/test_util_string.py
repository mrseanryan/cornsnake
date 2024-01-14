from parameterized import parameterized
import unittest

import util_string

class TestUtilString(unittest.TestCase):

    @ parameterized.expand([
        ('None', None, True),
        ('empty', '', True),
        ('only whitespace', '   \t\n', True),
        ('only hyphen', '  - \t\n', True),
        ('not empty', ' not empty  \t\n', False)
    ])
    def test_is_empty(self, description, input, expected):
        # Arrange
        # Act
        actual = util_string.is_empty(input)

        # Assert
        self.assertEqual(expected, actual, f'test: {description}')


if __name__ == '__main__':
    unittest.main()
