"""
Functions for extracting text from a PDF file and checking if a file is a PDF.

[Documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_pdf.html)
"""

def extract_text_from_pdf(filepath):
    """
    Function to extract text from a PDF file.

    Args:
    filepath (str): The path to the PDF file.

    Returns:
    str: The extracted text from the PDF file.
    """
    import fitz  # try avoid forcing install of PyMuPDF unless actually used
    with fitz.open(filepath) as doc:
        FORM_FEED = 12
        text = chr(FORM_FEED).join([page.get_text() for page in doc])
        return text

def is_pdf(filepath):
    """
    Function to check if a file is a PDF.

    Args:
    filepath (str): The path to the file.

    Returns:
    bool: True if the file is a PDF, False otherwise.
    """
    return filepath[-4:] == ".pdf"
