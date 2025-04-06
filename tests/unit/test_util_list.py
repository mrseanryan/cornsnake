from parameterized import parameterized
import unittest

from cornsnake import util_list


class TestUtilList(unittest.TestCase):
    @parameterized.expand(
        [
            ("[1,2,3] excluding [2]", [1, 2, 3], [2], [1, 3]),
            ("[1,2,3] excluding [3,1]", [1, 2, 3], [3, 1], [2]),
            ("[1,2,3] excluding [2,3,1]", [1, 2, 3], [2, 3, 1], []),
            ("[1,2,3] excluding [2,3,1,4]", [1, 2, 3], [2, 3, 1, 4], []),
            ("[1,2,3] excluding []", [1, 2, 3], [], [1, 2, 3]),
            ("[] excluding [1,2]", [], [1, 2], []),
            ("[] excluding []", [], [], []),
        ]
    )
    def test_excluding(self, description, input1, input2, expected):
        # Arrange
        # Act
        actual = util_list.excluding(input1, input2)

        # Assert
        self.assertEqual(expected, actual, f"test: {description}")

    @parameterized.expand(
        [
            ("first_or_none [1,2,3]", [1, 2, 3], 1),
            ("first_or_none [1]", [1], 1),
            ("first_or_none []", [], None),
            ("first_or_none [None]", [None], None),
        ]
    )
    def test_first_or_none(self, description, input, expected):
        # Arrange
        # Act
        actual = util_list.first_or_none(input)

        # Assert
        self.assertEqual(expected, actual, f"test: {description}")

    @parameterized.expand(
        [
            ("flatten [['a'],['b','c']]", ["a", ["b", "c"]], ["a", "b", "c"]),
            (
                "flatten [['aa'],['bb','cc']]",
                [["aa"], ["bb", "cc"]],
                ["aa", "bb", "cc"],
            ),
            ("flatten [[1],[2,3]]", [[1], [2, 3]], [1, 2, 3]),
            (
                "flatten [[1],[2,3,4,5,6],[7,8]]",
                [[1], [2, 3, 4, 5, 6], [7, 8]],
                [1, 2, 3, 4, 5, 6, 7, 8],
            ),
            ("flatten [[1,2,3]]", [[1, 2, 3]], [1, 2, 3]),
            ("flatten [[1]]", [[1]], [1]),
            ("flatten [[],[1]]", [[], [1]], [1]),
            ("flatten [[]]", [[]], []),
            ("flatten [[],[]]", [[], []], []),
            ("flatten []", [], []),
            ("flatten [[None]]", [[None]], [None]),
        ]
    )
    def test_flatten(self, description, input, expected):
        # Arrange
        # Act
        actual = util_list.flatten(input)

        # Assert
        self.assertEqual(expected, actual, f"test: {description}")

    @parameterized.expand(
        [
            ("list_with_first_or_empty [1,2,3]", [1, 2, 3], [1]),
            ("list_with_first_or_empty [1]", [1], [1]),
            ("list_with_first_or_empty []", [], []),
            ("list_with_first_or_empty [None]", [None], []),
        ]
    )
    def test_list_with_first_or_empty(self, description, input, expected):
        # Arrange
        # Act
        actual = util_list.list_with_first_or_empty(input)

        # Assert
        self.assertEqual(expected, actual, f"test: {description}")

    @parameterized.expand(
        [
            ("not_none_and_unique [1,2,3]", [1, 2, 3], [1, 2, 3]),
            ("not_none_and_unique [1,2,3,None]", [1, 2, 3, None], [1, 2, 3]),
            (
                "not_none_and_unique [1,2,3,3,4,4,4,None]",
                [1, 2, 3, 3, 4, 4, 4, None],
                [1, 2, 3, 4],
            ),
            ("not_none_and_unique [1]", [1], [1]),
            ("not_none_and_unique []", [], []),
            ("not_none_and_unique [None]", [None], []),
        ]
    )
    def test_not_none_and_unique(self, description, input, expected):
        # Arrange
        # Act
        actual = util_list.not_none_and_unique(input)

        # Assert
        self.assertEqual(expected, actual, f"test: {description}")

    @parameterized.expand(
        [
            ("unique [1,2,3]", [1, 2, 3], [1, 2, 3]),
            ("unique [None,1,2,3]", [None, 1, 2, 3], [1, 2, 3, None]),
            (
                "unique [None,1,2,3,3,4,4,4]",
                [None, 1, 2, 3, 3, 4, 4, 4],
                [1, 2, 3, 4, None],
            ),
            ("unique [1]", [1], [1]),
            ("unique []", [], []),
            ("unique [None]", [None], [None]),
            ("unique [None, None]", [None, None], [None]),
        ]
    )
    def test_unique(self, description, input, expected):
        # Arrange
        # Act
        actual = util_list.unique(input)

        # Assert
        self.assertEqual(expected, actual, f"test: {description}")

    @parameterized.expand(
        [
            ([], 5, []),
            (
                ["aa", "bb", "cc", "dd", "ee", "ff"],
                6,
                [["aa", "bb", "cc", "dd", "ee", "ff"]],
            ),
            (
                ["aa", "bb", "cc", "dd", "ee", "ff"],
                3,
                [["aa", "bb", "cc"], ["dd", "ee", "ff"]],
            ),
            (
                ["aa", "bb", "cc", "dd", "ee", "ff"],
                2,
                [["aa", "bb"], ["cc", "dd"], ["ee", "ff"]],
            ),
            (
                ["aa", "bb", "cc", "dd", "ee", "ff"],
                4,
                [["aa", "bb", "cc", "dd"], ["ee", "ff"]],
            ),
            (
                ["aa", "bb", "cc", "dd", "ee", "ff"],
                5,
                [
                    ["aa", "bb", "cc", "dd", "ee"],
                    ["ff"],
                ],  # we get a solitary item in the last chunk
            ),
        ]
    )
    def test_chunk(self, list_a, chunk_size, expected):
        # Arrange
        # Act
        actual = list(util_list.chunk(list_a, chunk_size))
        # Assert
        self.assertEqual(expected, actual)

    @parameterized.expand(
        [
            ([], 5, 5, []),
            (
                ["aa", "bb", "cc", "dd", "ee", "ff"],
                6,
                None,
                [["aa", "bb", "cc", "dd", "ee", "ff"]],
            ),
            (
                ["aa", "bb", "cc", "dd", "ee", "ff"],
                3,
                None,
                [["aa", "bb", "cc"], ["dd", "ee", "ff"]],
            ),
            (
                ["aa", "bb", "cc", "dd", "ee", "ff"],
                2,
                None,
                [["aa", "bb"], ["cc", "dd"], ["ee", "ff"]],
            ),
            (
                ["aa", "bb", "cc", "dd", "ee", "ff"],
                4,
                None,
                [["aa", "bb", "cc", "dd"], ["ee", "ff"]],
            ),
            (
                ["aa", "bb", "cc", "dd", "ee", "ff"],
                4,
                3,
                [
                    ["aa", "bb", "cc", "dd", "ee", "ff"]
                ],  # size 6 to have at least 2 in a chunk
            ),
            (
                ["aa", "bb", "cc", "dd", "ee", "ff"],
                5,
                2,
                [
                    ["aa", "bb", "cc", "dd", "ee", "ff"]
                ],  # size 6 to have at least 2 in a chunk
            ),
            (
                ["aa", "bb", "cc", "dd", "ee", "ff", "gg"],
                3,
                None,
                [["aa", "bb", "cc"], ["dd", "ee", "ff"], ["gg"]],
            ),
            (
                ["aa", "bb", "cc", "dd", "ee", "ff", "gg"],
                3,
                2,
                [
                    ["aa", "bb", "cc"],
                    ["dd", "ee", "ff", "gg"],
                ],  # last chunk has 4, to avoid a last chunk with < 2
            ),
            (
                ["aa", "bb", "cc", "dd", "ee", "ff", "gg"],
                5,
                None,
                [["aa", "bb", "cc", "dd", "ee"], ["ff", "gg"]],
            ),
            (
                ["aa", "bb", "cc", "dd", "ee", "ff", "gg"],
                5,
                2,
                [["aa", "bb", "cc", "dd", "ee"], ["ff", "gg"]],
            ),
            (
                ["aa", "bb", "cc", "dd", "ee", "ff", "gg"],
                5,
                3,
                [
                    ["aa", "bb", "cc", "dd", "ee", "ff", "gg"]
                ],  # last chunk is full, to avoid a last chunk with < 3
            ),
        ]
    )
    def test_chunk_merge_orphans(self, list_a, chunk_size, min_chunk_size, expected):
        # Arrange
        # Act
        if not min_chunk_size:
            min_chunk_size = 1
        actual = list(
            util_list.chunk(list_a, chunk_size, min_chunk_size=min_chunk_size)
        )
        # Assert
        self.assertEqual(expected, actual)

    def test_chunk_size_zero_raises(self):
        # Arrange
        # Act, Assert
        with self.assertRaises(ValueError):
            list(util_list.chunk(list_a=[], CHUNK_SIZE=0))

    def test_bad_min_chunk_size_raises(self):
        # Arrange
        list_a = []

        # Act, Assert
        with self.assertRaises(ValueError):
            list(util_list.chunk(list_a, CHUNK_SIZE=2, min_chunk_size=3))

    @parameterized.expand(
        [
            ([], []),
            (["aa", "bb", "cc"], ["aa", "bb", "cc"]),
            (["aa", "", "cc"], ["aa", "cc"]),
            (["aa", " ", "cc"], ["aa", " ", "cc"]),
            (["aa", " ", " cc "], ["aa", " ", " cc "]),
        ]
    )
    def test_remove_empty_strings(self, list_a, expected):
        # Arrange
        # Act
        actual = util_list.remove_empty_strings(list_a)
        # Assert
        self.assertEqual(expected, actual)

    @parameterized.expand(
        [
            ([], []),
            (["aa", "bb", "cc"], ["aa", "bb", "cc"]),
            (["aa", "", "cc"], ["aa", "", "cc"]),
            (["aa", " ", "cc"], ["aa", "", "cc"]),
            (["aa", " ", " cc "], ["aa", "", "cc"]),
        ]
    )
    def test_strip_strings(self, list_a, expected):
        # Arrange
        # Act
        actual = util_list.strip_strings(list_a)
        # Assert
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
