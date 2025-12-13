from flask import Flask, request, render_template
import os
import subprocess

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if "file" not in request.files:
            return "No file uploaded"

        file = request.files["file"]
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        output_path = os.path.join(UPLOAD_FOLDER, "output.mp4")

        command = [
            "ffmpeg",
            "-i", filepath,
            "-vf", "scale=204:360",
            output_path
        ]

        subprocess.run(command, check=True)

        return f"Video saved: {output_path}"

    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
from flask import Flask, request, render_template
import os
import subprocess

app = Flask(__name__)

if not os.path.exists("uploads"):
    os.makedirs("uploads")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files["file"]
        filepath = os.path.join("uploads", file.filename)
        file.save(filepath)

        output_path = os.path.join("uploads", "output.mp4")

        command = [
            "ffmpeg",
            "-i", filepath,
            "-vf", "scale=204:360",
            output_path
        ]

        subprocess.run(command)

        return f"Video saved: {output_path}"

    return render_template("index.html")

if __name__ == "__main__":
    app.run()

