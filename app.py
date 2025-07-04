from flask import Flask, jsonify
import os
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def hello_world():
    return jsonify(
        {
            "message": "Hello, World!",
            "timestamp": datetime.now().isoformat(),
            "version": "1.0.0",
            "environment": os.getenv("FLASK_ENV", "production"),
        }
    )


@app.route("/health")
def health_check():
    return jsonify({"status": "healthy", "timestamp": datetime.now().isoformat()})


@app.route("/api/info")
def app_info():
    return jsonify(
        {
            "app_name": "HelloWorld API",
            "version": "1.0.0",
            "description": "A production-ready Flask Hello World application",
            "endpoints": [
                {"path": "/", "method": "GET", "description": "Hello World message"},
                {
                    "path": "/health",
                    "method": "GET",
                    "description": "Health check endpoint",
                },
                {
                    "path": "/api/info",
                    "method": "GET",
                    "description": "Application information",
                },
            ],
        }
    )


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    debug = os.getenv("FLASK_ENV") == "development"
    app.run(host="0.0.0.0", port=port, debug=debug)
