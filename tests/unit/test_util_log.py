import unittest

from cornsnake import util_log

WINDOWS_SEP = "\\"
MAC_SEP = "/"


class TestUtilLog(unittest.TestCase):
    def test_mask_sensitive_text__windows(self):
        # Arrange

        # Act, Assert
        text = r"C:\Users\Bob.Jones\my-file.txt"
        expected = r"C:\Users\<masked>\my-file.txt"
        actual = util_log.mask_sensitive_text(text, WINDOWS_SEP)
        self.assertEqual(expected, actual)

    def test_mask_sensitive_text_git__windows(self):
        # Arrange

        # Act, Assert
        # Even on Windows, git config uses unix-style paths:
        text = "file:C:/Users/John.Jones/.gitconfig      alias.st=status"
        expected = "file:C:/Users/<masked>/.gitconfig      alias.st=status"
        actual = util_log.mask_sensitive_text(text, WINDOWS_SEP)
        self.assertEqual(expected, actual)

    def test_mask_sensitive_text__mac(self):
        # Arrange

        # Act, Assert
        text = "/Users/Bob.Jones/my-file.txt"
        expected = "/Users/<masked>/my-file.txt"
        actual = util_log.mask_sensitive_text(text, MAC_SEP)
        self.assertEqual(expected, actual)

    def test_mask_normal_text__windows(self):
        # Arrange

        # Act, Assert
        text = r"C:\ Some text Users\ Bob \my-file.txt"
        expected = text
        actual = util_log.mask_sensitive_text(text, WINDOWS_SEP)
        self.assertEqual(expected, actual)

    def test_mask_normal_text__mac(self):
        # Arrange

        # Act, Assert
        text = "/ Users / Something here /my-file.txt"
        expected = text
        actual = util_log.mask_sensitive_text(text, MAC_SEP)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
