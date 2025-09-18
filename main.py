import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Cloud Run Secret Test: service is running!"

@app.route("/check-secret")
def check_secret():
    secret_path = os.environ.get("SECRET_PATH", "/secrets/my-secret.json")

    try:
        with open(secret_path, "r") as f:
            content = f.read(100)  # read first 100 chars
        return f"✅ Secret file is accessible!\n\nFirst 100 chars:\n{content}"
    except Exception as e:
        return f"❌ Error accessing secret: {str(e)}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
