from app.sentiment import analyze_sentiment

def test_positive():
    assert analyze_sentiment("This is a good product") == "positive"

def test_negative():
    assert analyze_sentiment("This is the worst experience") == "negative"

def test_neutral():
    assert analyze_sentiment("This is a product") == "neutral"
