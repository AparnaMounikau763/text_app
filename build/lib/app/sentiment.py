POSITIVE_WORDS = ["good", "great", "happy", "excellent", "amazing"]
NEGATIVE_WORDS = ["bad", "sad", "worst", "poor"]

def analyze_sentiment(text):
    text = text.lower()

    score = 0
    for word in POSITIVE_WORDS:
        if word in text:
            score += 1

    for word in NEGATIVE_WORDS:
        if word in text:
            score -= 1

    if score > 0:
        return "positive"
    elif score < 0:
        return "negative"
    return "neutral"
