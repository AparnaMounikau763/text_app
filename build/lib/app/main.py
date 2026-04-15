from app.processor import preprocess_text
from app.validator import validate_text
from app.sentiment import analyze_sentiment

def run_pipeline(text):
    processed = preprocess_text(text)
    validate_text(processed)
    result = analyze_sentiment(processed)
    return result