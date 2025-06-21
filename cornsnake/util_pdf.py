"""
Functions for extracting text from a PDF file and checking if a file is a PDF.

[Documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_pdf.html)
"""


def extract_text_from_pdf(
    filepath: str, start_page: int = -1, end_page: int = -1
) -> str:
    """
    Function to extract text from a PDF file.

    Args:
    filepath (str): The path to the PDF file.
    start_page (int, optional): The page to start extracting from (1-indexed).
    end_page (int, optional): The last page to extract (1-indexed).

    Returns:
    str: The extracted text from the PDF file.
    """
    import fitz  # try avoid forcing install of PyMuPDF unless actually used

    doc = fitz.open(filepath)
    text = []

    # Clamp page numbers to valid range
    start = max(start_page, 1)
    end = min(end_page, doc.page_count)
    if end == -1:
        end = doc.page_count

    for page_num in range(start - 1, end):  # zero-based index for fitz
        page = doc.load_page(page_num)
        text.append(page.get_text())

    doc.close()
    return "\n".join(text)


def is_pdf(filepath: str) -> bool:
    """
    Function to check if a file is a PDF.

    Args:
    filepath (str): The path to the file.

    Returns:
    bool: True if the file is a PDF, False otherwise.
    """
    return filepath[-4:] == ".pdf"
