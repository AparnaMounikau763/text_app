from app.main import run_pipeline

def test_system_positive():
    result = run_pipeline("This is GREAT!!!")
    assert result == "positive"

def test_system_negative():
    result = run_pipeline("This is the worst experience")
    assert result == "negative"

def test_system_neutral():
    result = run_pipeline("This is a product")
    assert result == "neutral"