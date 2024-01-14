def is_empty(text):
    if text is None:
        return True
    stripped = text.strip()
    return stripped == '' or stripped == '-'
