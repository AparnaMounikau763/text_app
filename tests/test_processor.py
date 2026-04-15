from app.processor import preprocess_text

def test_empty_string():
    assert preprocess_text("") == ""

def test_only_special_characters():
    assert preprocess_text("!!!@@@###") == ""

def test_only_numbers():
    assert preprocess_text("123456") == ""