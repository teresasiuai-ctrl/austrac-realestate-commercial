from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "product": "AUSTRAC Real Estate AI Agent",
        "status": "running",
        "version": "commercial-mvp"
    })

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json

    return jsonify({
        "status": "received",
        "analysis_type": "compliance-check",
        "input": data,
        "result": "placeholder - AI engine not connected yet"
    })

if __name__ == "__main__":
    app.run(debug=True)
