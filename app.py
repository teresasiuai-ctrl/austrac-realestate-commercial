from flask import Flask, request, jsonify

app = Flask(__name__)

def load_system_prompt():
    try:
        with open("prompts/system_prompt.md", "r") as f:
            return f.read()
    except:
        return "System prompt not found"

SYSTEM_PROMPT = load_system_prompt()

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
        "system_prompt_loaded": True,
        "analysis_type": "compliance-check",
        "input": data,
        "note": "AI engine not connected yet"
    })

if __name__ == "__main__":
    app.run(debug=True)
