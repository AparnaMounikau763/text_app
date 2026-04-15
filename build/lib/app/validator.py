def validate_text(text):
    if not text:
        raise ValueError("Text cannot be empty")

    if len(text) < 3:
        raise ValueError("Text too short")

    return True
