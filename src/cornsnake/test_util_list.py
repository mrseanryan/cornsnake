from parameterized import parameterized
import unittest

import util_list

class TestUtilList(unittest.TestCase):

    @ parameterized.expand([
        ('[1,2,3] excluding [2]', [1, 2, 3], [2], [1, 3]),
        ('[1,2,3] excluding [3,1]', [1, 2, 3], [3, 1], [2]),
        ('[1,2,3] excluding [2,3,1]', [1, 2, 3], [2, 3, 1], []),
        ('[1,2,3] excluding [2,3,1,4]', [1, 2, 3], [2, 3, 1, 4], []),
        ('[1,2,3] excluding []', [1, 2, 3], [], [1, 2, 3]),
        ('[] excluding [1,2]', [], [1, 2], []),
        ('[] excluding []', [], [], []),
    ])
    def test_excluding(self, description, input1, input2, expected):
        # Arrange
        # Act
        actual = util_list.excluding(input1, input2)

        # Assert
        self.assertEqual(expected, actual, f'test: {description}')

    @ parameterized.expand([
        ('first_or_none [1,2,3]', [1, 2, 3], 1),
        ('first_or_none [1]', [1], 1),
        ('first_or_none []', [], None),
        ('first_or_none [None]', [None], None),
    ])
    def test_first_or_none(self, description, input, expected):
        # Arrange
        # Act
        actual = util_list.first_or_none(input)

        # Assert
        self.assertEqual(expected, actual, f'test: {description}')

    @ parameterized.expand([
        ("flatten [['a'],['b','c']]", ['a', ['b', 'c']], ['a', 'b', 'c']),
        ("flatten [['aa'],['bb','cc']]", [
         ['aa'], ['bb', 'cc']], ['aa', 'bb', 'cc']),
        ('flatten [[1],[2,3]]', [[1], [2, 3]], [1, 2, 3]),
        ('flatten [[1],[2,3,4,5,6],[7,8]]', [
         [1], [2, 3, 4, 5, 6], [7, 8]], [1, 2, 3, 4, 5, 6, 7, 8]),
        ('flatten [[1,2,3]]', [[1, 2, 3]], [1, 2, 3]),
        ('flatten [[1]]', [[1]], [1]),
        ('flatten [[],[1]]', [[], [1]], [1]),
        ('flatten [[]]', [[]], []),
        ('flatten [[],[]]', [[], []], []),
        ('flatten []', [], []),
        ('flatten [[None]]', [[None]], [None]),
    ])
    def test_flatten(self, description, input, expected):
        # Arrange
        # Act
        actual = util_list.flatten(input)

        # Assert
        self.assertEqual(expected, actual, f'test: {description}')

    @ parameterized.expand([
        ('list_with_first_or_empty [1,2,3]', [1, 2, 3], [1]),
        ('list_with_first_or_empty [1]', [1], [1]),
        ('list_with_first_or_empty []', [], []),
        ('list_with_first_or_empty [None]', [None], []),
    ])
    def test_list_with_first_or_empty(self, description, input, expected):
        # Arrange
        # Act
        actual = util_list.list_with_first_or_empty(input)

        # Assert
        self.assertEqual(expected, actual, f'test: {description}')

    @ parameterized.expand([
        ('not_none_and_unique [1,2,3]', [1, 2, 3], [1, 2, 3]),
        ('not_none_and_unique [1,2,3,None]', [1, 2, 3, None], [1, 2, 3]),
        ('not_none_and_unique [1,2,3,3,4,4,4,None]',
         [1, 2, 3, 3, 4, 4, 4, None], [1, 2, 3, 4]),
        ('not_none_and_unique [1]', [1], [1]),
        ('not_none_and_unique []', [], []),
        ('not_none_and_unique [None]', [None], []),
    ])
    def test_not_none_and_unique(self, description, input, expected):
        # Arrange
        # Act
        actual = util_list.not_none_and_unique(input)

        # Assert
        self.assertEqual(expected, actual, f'test: {description}')

    @ parameterized.expand([
        ('unique [1,2,3]', [1, 2, 3], [1, 2, 3]),
        ('unique [None,1,2,3]', [None, 1, 2, 3], [1, 2, 3, None]),
        ('unique [None,1,2,3,3,4,4,4]',
         [None, 1, 2, 3, 3, 4, 4, 4], [1, 2, 3, 4, None]),
        ('unique [1]', [1], [1]),
        ('unique []', [], []),
        ('unique [None]', [None], [None]),
        ('unique [None, None]', [None, None], [None]),
    ])
    def test_unique(self, description, input, expected):
        # Arrange
        # Act
        actual = util_list.unique(input)

        # Assert
        self.assertEqual(expected, actual, f'test: {description}')


if __name__ == '__main__':
    unittest.main()
