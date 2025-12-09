from flask import Flask, request, render_template
from moviepy.editor import VideoFileClip
import os

app = Flask(__name__)

if not os.path.exists("uploads"):
    os.makedirs("uploads")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files["file"]
        filepath = os.path.join("uploads", file.filename)
        file.save(filepath)

        clip = VideoFileClip(filepath)
        output = filepath.rsplit(".", 1)[0] + ".mp3"
        clip.audio.write_audiofile(output)

        return f"Converted Successfully! Saved as: {output}"

    return render_template("index.html")

if __name__ == "__main__":
    app.run()


