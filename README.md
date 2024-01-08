# Sentiment Analysis Web Application with Flask

Welcome to the Sentiment Analysis Web Application! This web application is built using Flask and utilizes the NLTK library for sentiment analysis. Users can input text, and the application will analyze the sentiment, providing a visual representation through 0-1 bar charts.

## Features

- **Sentiment Analysis**: Enter any text, and the application will analyze whether it is positive, negative, or neutral.
- **Bar Charts**: Visual representation of sentiment scores in the form of 0-1 bar charts.
- **Interactive Chatbot**: An interactive chatbot is available to explain how the sentiment analysis is performed.

## How it Works

The sentiment analysis is carried out using the `SentimentIntensityAnalyzer` from the NLTK library. Below is a simple example using the analyzer:

```python
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()
scores = sia.polarity_scores("I am so happy!")
print(scores)
