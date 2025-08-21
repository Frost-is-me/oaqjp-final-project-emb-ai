"""Flask app for emotion detection."""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emot_detector():
    """Detect emotion from query text."""
    text_to_analyze = request.args.get("textToAnalyze")
    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid text! Please try again!"
    response = emotion_detector(text_to_analyze)
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    return (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """Render index page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
