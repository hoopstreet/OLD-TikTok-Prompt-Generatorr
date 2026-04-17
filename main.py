import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>TikTok-Prompt-Generator: Online</h1><p>Status: Phoenix Architecture Active</p>"

if __name__ == "__main__":
    # HF requires port 7860
    port = int(os.environ.get("PORT", 7860))
    app.run(host='0.0.0.0', port=port)
