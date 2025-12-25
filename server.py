"""
server.py

Flask web application for Emotion Detection.
Uses the EmotionDetection package to analyze customer feedback and
returns emotion scores and dominant emotion.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Create Flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_function():
    """
    Endpoint to analyze emotions from a text statement.
    Query Parameter:
        textToAnalyze (str): The input text to analyze.

    Returns:
        str: Formatted response including emotion scores and dominant emotion.
             If input is blank, returns an error message.
    """
    # Get input from query parameter
    text_to_analyze = request.args.get('textToAnalyze', '')

    # Call emotion_detector function
    response = emotion_detector(text_to_analyze)

    # Handle blank input
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Format the response text
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return response_text

@app.route("/")
def render_index_page():
    """
    Endpoint to render the index HTML page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    """
    Main entry point to run the Flask app.
    Listens on all addresses, port 5000.
    """
    app.run(host="0.0.0.0", port=5000)

