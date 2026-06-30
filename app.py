
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return {"status": "AUSTRAC Real Estate AI Agent running"}

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    return {
        "message": "Analysis endpoint ready",
        "input_received": data
    }

if __name__ == "__main__":
    app.run(debug=True)
