from parameterized import parameterized
import unittest

from cornsnake import util_string


class TestUtilString(unittest.TestCase):
    @parameterized.expand(
        [
            ("None", None, True),
            ("empty", "", True),
            ("only whitespace", "   \t\n", True),
            ("only hyphen", "  - \t\n", True),
            ("not empty", " not empty  \t\n", False),
        ]
    )
    def test_is_empty(self, description, input, expected):
        # Arrange
        # Act
        actual = util_string.is_empty(input)

        # Assert
        self.assertEqual(expected, actual, f"test: {description}")

    @parameterized.expand(
        [
            (
                "convert invalid file name",
                "temp\\x.txt",
                "^[a-zA-Z0-9_\.]+$",
                "=",
                "temp=x.txt",
            ),
            (
                "convert to letters only",
                "??asdfs 234 : 123^%&%.my .txt",
                "^[a-zA-Z]+$",
                "X",
                "XXasdfsXXXXXXXXXXXXXXXmyXXtxt",
            ),
            # no-op tests:
            ("no-op", "all letters OK", "^[a-zA-Z ]+$", "!", "all letters OK"),
        ]
    )
    def test_filter_string_via_regex(
        self, description, text, regex, replacement_char, expected
    ):
        # Arrange

        # Act
        actual = util_string.filter_string_via_regex(
            text=text, regex=regex, replacement_char=replacement_char
        )

        # Assert
        self.assertEqual(expected, actual, f"test: {description}")

    @parameterized.expand(
        [
            ("empty", "", 0),
            ("space", " ", 0),
            ("1 word", "one", 1),
            ("2 word", "one two", 2),
            (
                "Simple sentence",
                "Functions for working with strings: filtering by regex, checking if is mostly empty, replacing whilst maintaining casing, splitting into lines, counting words.",
                22,
            ),
        ]
    )
    def test_count_words(self, description, text, expected):
        # Arrange

        # Act
        actual = util_string.count_words(text=text)

        # Assert
        self.assertEqual(expected, actual, f"test: {description}")


if __name__ == "__main__":
    unittest.main()
