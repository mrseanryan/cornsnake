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

    @parameterized.expand(
        [
            ("empty", "", ""),
            ("short", "short", "short"),
            (
                "long",
                "This is a very long string that should be shortened.",
                "This is a very long string th…",
            ),
            (
                "exact length",
                "This is exactly thirty charact",
                "This is exactly thirty charact",
            ),
        ]
    )
    def test_shorten(self, description, text, expected):
        # Arrange
        max_length = 30

        # Act
        actual = util_string.shorten(s=text, max_length=max_length)

        # Assert
        self.assertEqual(
            expected,
            actual,
            f"test: {description} - Shortened string does not match expected.",
        )

    @parameterized.expand(
        [
            ("empty", "", ""),
            ("short", "short", "short"),
            (
                "long",
                "This is a very long string that should be shortened.",
                "This is a very…d be shortened.",
            ),
            (
                "exact length",
                "This is exactly thirty charact",
                "This is exactly thirty charact",
            ),
        ]
    )
    def test_shorten_at_middle(self, description, text, expected):
        # Arrange
        max_length = 30

        # Act
        actual = util_string.shorten_at_middle(s=text, max_length=max_length)

        # Assert
        self.assertEqual(
            expected,
            actual,
            f"test: {description} - Shortened string does not match expected.",
        )

    @parameterized.expand(
        [
            ("empty", "", ""),
            ("short", "short", "short"),
            (
                "long",
                "This is a very long string that should be shortened.",
                "…ing that should be shortened.",
            ),
            (
                "exact length",
                "This is exactly thirty charact",
                "This is exactly thirty charact",
            ),
        ]
    )
    def test_shorten_at_start(self, description, text, expected):
        # Arrange
        max_length = 30

        # Act
        actual = util_string.shorten_at_start(s=text, max_length=max_length)

        # Assert
        self.assertEqual(
            expected,
            actual,
            f"test: {description} - Shortened string does not match expected.",
        )

    @parameterized.expand(
        [
            ("empty", "", []),
            ("short", "short", ["short"]),
            (
                "long",
                "This is a very long string that should be split into multiple lines.",
                [
                    "This is a very long string that should be split",
                    "into multiple lines.",
                ],
            ),
            (
                "split at word boundaries",
                "This is a long text that needs to be split into lines of maximum length.",
                [
                    "This is a long text that needs to be split into",
                    "lines of maximum length.",
                ],
            ),
        ]
    )
    def test_split_into_lines(self, description, text, expected):
        # Arrange
        max_length = 50

        # Act
        actual = util_string.split_into_lines(text=text, max_length=max_length)

        # Assert
        self.assertEqual(
            expected, actual, f"test: {description} - Lines do not match expected."
        )
        self.assertTrue(
            all(len(line) <= max_length for line in actual),
            f"test: {description} - Some lines exceed max length of {max_length}.",
        )

    @parameterized.expand(
        [
            ("empty", "", []),
            ("short", "short", ["short"]),
            (
                "long",
                "This is a very long string that should be split into multiple lines.",
                [
                    "This is a very long string that should be split",
                    "into multiple lines.",
                ],
            ),
            (
                "split at word boundaries",
                "This is a long text that needs to be split into lines of maximum length.",
                [
                    "This is a long text that needs to be split into",
                    "lines of maximum length.",
                ],
            ),
        ]
    )
    def test_split_into_lines(self, description, text, expected):
        # Arrange
        max_length = 50

        # Act
        actual = util_string.split_into_lines(text=text, max_length=max_length)

        # Assert
        self.assertEqual(
            expected, actual, f"test: {description} - Lines do not match expected."
        )
        self.assertTrue(
            all(len(line) <= max_length for line in actual),
            f"test: {description} - Some lines exceed max length of {max_length}.",
        )


if __name__ == "__main__":
    unittest.main()
