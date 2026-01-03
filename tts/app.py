from tts import synthesize_speech
from flask import Flask, request, send_file

app = Flask(__name__)

@app.route("/synthesize", methods=["POST"])
def synthesize():
    data = request.json
    text = data.get("text", "")
    output_voice = data.get("voice", "af_heart")
    synthesize_speech(text, output_voice)
    return send_file("0.wav", mimetype="audio/wav")

if __name__ == "__main__":
    app.run(debug=True, port=5001)