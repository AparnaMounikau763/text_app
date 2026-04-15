from app.processor import preprocess_text
from app.validator import validate_text
from app.sentiment import analyze_sentiment

def test_full_pipeline():
    text = "This is AMAZING!!!"

    processed = preprocess_text(text)
    validate_text(processed)
    result = analyze_sentiment(processed)

    assert result == "positive"