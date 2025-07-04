from flask import Flask, jsonify, render_template
import os
from datetime import datetime
import time

app = Flask(__name__)
start_time = time.time()


@app.route("/")
def hello_world():
    uptime_seconds = int(time.time() - start_time)
    uptime_hours = uptime_seconds // 3600
    uptime_display = f"{uptime_hours}h" if uptime_hours > 0 else f"{uptime_seconds}s"

    data = {
        "message": "Hello, World!",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC"),
        "version": "1.0.0",
        "environment": os.getenv("FLASK_ENV", "production").title(),
        "uptime": uptime_display,
    }
    return render_template("index.html", data=data)


@app.route("/api/hello")
def api_hello():
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
