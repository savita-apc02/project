from flask import Flask, request, render_template
from moviepy.editor import VideoFileClip
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files["file"]
        filepath = os.path.join("uploads", file.filename)
        file.save(filepath)

        clip = VideoFileClip(filepath)
        output = filepath.replace(".mp4", ".mp3")
        clip.audio.write_audiofile(output)

        return "Converted Successfully!"

    return render_template("index.html")


if __name__ == "__main__":
    app.run()
