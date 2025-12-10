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

        # FFmpeg command run
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
