import unittest

from cornsnake import util_log


class TestUtilLog(unittest.TestCase):
    def test_mask_sensitive_text__windows(self):
        # Arrange

        # Act, Assert
        text = r"C:\Users\Bob.Jones\my-file.txt"
        expected = r"C:\Users\<masked>\my-file.txt"
        actual = util_log.mask_sensitive_text(text)
        self.assertEqual(expected, actual)

    def test_mask_sensitive_text_git__windows(self):
        # Arrange

        # Act, Assert
        # Even on Windows, git config uses unix-style paths:
        text = "file:C:/Users/John.Jones/.gitconfig      alias.st=status"
        expected = "file:C:/Users/<masked>/.gitconfig      alias.st=status"
        actual = util_log.mask_sensitive_text(text)
        self.assertEqual(expected, actual)

    def test_mask_sensitive_text_git_multiline__windows(self):
        # Arrange

        # Act, Assert
        # Even on Windows, git config uses unix-style paths.
        # - also, parts of the text may have already been masked
        text = """
file:C:/Program Files/Git/etc/gitconfig\tcredential.helper = <masked>
file:C:/Program Files/Git/etc/gitconfig\tcredential.https://dev.azure.com.usehttppath = <masked>
file:C:\\Program Files\\Git\\etc\\gitconfig\\tcredential.https://dev.azure.com.usehttppath = <masked>
file:C:/Program Files/Git/etc/gitconfig\tinit.defaultbranch=master
file:C:/Users/Mary.Jane/.gitconfig\tfilter.lfs.clean=git-lfs clean -- %f
file:C:/Users/Mary.Jane/.gitconfig\tfilter.lfs.smudge=git-lfs smudge -- %f
file:C:/Users/Mary.Jane/.gitconfig\tfilter.lfs.process=git-lfs filter-process
file:C:/Users/Mary.Jane/.gitconfig\tfilter.lfs.required=true
file:C:/Users/Mary.Jane/.gitconfig\tcore.autocrlf=false
file:C:\\Users\\Mary.Jane\\.gitconfig\tcore.autocrlf=false
file:C:/Users/Mary.Jane/.gitconfig\tcore.editor="C:/Program Files (x86)/GitExtensions/GitExtensions.exe" fileeditor
file:C:/Users/Mary.Jane/.gitconfig\tuser.name = <masked>
file:C:/Users/Mary.Jane/.gitconfig\tuser.email = <masked>
file:C:/Users/Mary.Jane/.gitconfig\trerere.enabled=true
file:C:/Users/Mary.Jane/.gitconfig\tpull.rebase=true
"""
        expected = """
file:C:/Program Files/Git/etc/gitconfig\tcredential.helper = <masked>
file:C:/Program Files/Git/etc/gitconfig\tcredential.https://dev.azure.com.usehttppath = <masked>
file:C:\\Program Files\\Git\\etc\\gitconfig\\tcredential.https://dev.azure.com.usehttppath = <masked>
file:C:/Program Files/Git/etc/gitconfig\tinit.defaultbranch=master
file:C:/Users/<masked>/.gitconfig\tfilter.lfs.clean=git-lfs clean -- %f
file:C:/Users/<masked>/.gitconfig\tfilter.lfs.smudge=git-lfs smudge -- %f
file:C:/Users/<masked>/.gitconfig\tfilter.lfs.process=git-lfs filter-process
file:C:/Users/<masked>/.gitconfig\tfilter.lfs.required=true
file:C:/Users/<masked>/.gitconfig\tcore.autocrlf=false
file:C:\\Users\\<masked>\\.gitconfig\tcore.autocrlf=false
file:C:/Users/<masked>/.gitconfig\tcore.editor="C:/Program Files (x86)/GitExtensions/GitExtensions.exe" fileeditor
file:C:/Users/<masked>/.gitconfig\tuser.name = <masked>
file:C:/Users/<masked>/.gitconfig\tuser.email = <masked>
file:C:/Users/<masked>/.gitconfig\trerere.enabled=true
file:C:/Users/<masked>/.gitconfig\tpull.rebase=true
"""

        actual = util_log.mask_sensitive_text(text)
        self.assertEqual(expected, actual)

    def test_mask_sensitive_text__mac(self):
        # Arrange

        # Act, Assert
        text = "/Users/Bob.Jones/my-file.txt"
        expected = "/Users/<masked>/my-file.txt"
        actual = util_log.mask_sensitive_text(text)
        self.assertEqual(expected, actual)

    def test_mask_normal_text__windows(self):
        # Arrange

        # Act, Assert
        text = r"C:\ Some text Users\ Bob \my-file.txt"
        expected = text
        actual = util_log.mask_sensitive_text(text)
        self.assertEqual(expected, actual)

    def test_mask_normal_text__mac(self):
        # Arrange

        # Act, Assert
        text = "/ Users / Something here /my-file.txt"
        expected = text
        actual = util_log.mask_sensitive_text(text)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
