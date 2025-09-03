from parameterized import parameterized
import unittest

from cornsnake import util_yaml


class TestUtilYaml(unittest.TestCase):
    @parameterized.expand(
        [
            ("empty", {}, {}),
            ("not empty", {"key": "value"}, {"key": "value"}),
            (
                "mixed order",
                {
                    "key2": ["value2", "value1"],
                    "key1": {
                        "subkey": {
                            "subsubkey2": "subsubvalue",
                            "subsubkey1": "subsubvalue",
                        }
                    },
                },
                {
                    "key1": {
                        "subkey": {
                            "subsubkey1": "subsubvalue",
                            "subsubkey2": "subsubvalue",
                        }
                    },
                    "key2": ["value1", "value2"],
                },
            ),
        ]
    )
    def test_is_empty(
        self, description: str, input: util_yaml.YAMLType, expected: util_yaml.YAMLType
    ):
        # Arrange
        # Act
        actual = util_yaml.deep_sort(data=input)

        # Assert
        self.assertEqual(expected, actual, f"test: {description}")
