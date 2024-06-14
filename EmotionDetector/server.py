from flask import Flask, render_template, request, jsonify
from emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def emotions():
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)

    if response['Dominant Emotion'] == None:
        return "Invalid text! Please try again!"
    
    else:
        return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)