FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
RUN pip install .

CMD ["python", "-c", "from app.sentiment import analyze_sentiment; print(analyze_sentiment('good'))"]