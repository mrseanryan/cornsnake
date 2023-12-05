MARKDOWN_COLUMN_SEPARATOR = "|"

MARKDOWN_COLUMN_INDICATOR = "---"

def add_row_separator(column_count):
    row = MARKDOWN_COLUMN_SEPARATOR
    while column_count > 0:
        row += MARKDOWN_COLUMN_INDICATOR + MARKDOWN_COLUMN_SEPARATOR
        column_count -= 1
    return row

def generate_markdown_image(path_to_image, caption):
    return f"![{caption}]({path_to_image} \"{caption}\" )"

def generate_italicised(text):
    return f"*{text}*"
