from flask import Flask, render_template, request, jsonify
from nltk.sentiment import SentimentIntensityAnalyzer
import re

app = Flask(__name__)

sia = SentimentIntensityAnalyzer()

questions_patterns = [
    {
        "pattern": r"What is the Sentiment Intensity Analyzer \(SIA\)\?",
        "response": "The Sentiment Intensity Analyzer (SIA) is a part of the Natural Language Toolkit (NLTK)."
    },
    {
        "pattern": r"How does SIA evaluate the sentiment of a piece of text\?",
        "response": "SIA evaluates the sentiment of a piece of text using a pre-trained model."
    },
    {
        "pattern": r"What is the key idea behind SIA\?",
        "response": "The key idea behind SIA is to assign a sentiment score to a given text. The score ranges from -1 (most negative) to 1 (most positive)."
    },
    {
        "pattern": r"What features does the analyzer use to assess the sentiment of the text\?",
        "response": "The analyzer uses a combination of lexical, grammatical, and semantic features to assess the sentiment of the text."
    },
    {
        "pattern": r"How does SIA calculate the sentiment polarity score for each token in the text\?",
        "response": "SIA calculates a sentiment polarity score for each token in the text."
    },
    {
        "pattern": r"How are these scores combined to get an overall compound score\?",
        "response": "These scores are combined to get an overall compound score."
    },
    {
        "pattern": r"What does the compound score represent\?",
        "response": "The compound score provides a single, normalized score for the sentiment of the entire text. Positive values indicate positive sentiment, negative values indicate negative sentiment, and values close to zero suggest a more neutral sentiment."
    },
    {
        "pattern": r"What should be kept in mind about SIA\?",
        "response": "Keep in mind that SIA is a rule-based approach and may not capture the complexity of all types of texts. It's particularly useful for quick sentiment analysis tasks."
    },
    {
        "pattern": r"(Tell me about SIA|Explain SIA|How does SIA work)",
        "response": "SIA, or Sentiment Intensity Analyzer, is a tool that evaluates the sentiment of a piece of text. It analyzes various features to determine the overall sentiment, providing a score from -1 (most negative) to 1 (most positive)."
    },
    {
        "pattern": r"(keyword|extract keywords|key terms)",
        "response": "Keyword extraction is a process of identifying and extracting important words or phrases from a piece of text. It helps to understand the main topics and themes within the text."
    },
    {
        "pattern": r"(.*)",
        "response": "I'm sorry, I don't have a response for that."
    }
]

def get_response(user_message):
    for pattern in questions_patterns:
        if re.search(pattern["pattern"], user_message, re.IGNORECASE):
            return pattern["response"]

    return "I'm sorry, I don't have a response for that."

def analysis(input_text):
    return sia.polarity_scores(input_text)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    input_text = data['text']
    sentiment_scores = analysis(input_text)
    
    # Return sentiment analysis results as JSON
    return jsonify({
        'pos': sentiment_scores['pos'],
        'neg': sentiment_scores['neg'],
        'neu': sentiment_scores['neu']
    })

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    bot_response = get_response(user_message)
    return jsonify({'message': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
