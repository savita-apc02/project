from flask import Flask, request, render_template
import os
import subprocess

app = Flask(__name__)

# uploads folder create
if not os.path.exists("uploads"):
    os.makedirs("uploads")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":

        file = request.files["file"]
        filepath = os.path.join("uploads", file.filename)
        file.save(filepath)

        # output file name
        output = filepath.rsplit(".", 1)[0] + ".mp3"

        # ffmpeg convert command
        command = f"ffmpeg -i \"{filepath}\" \"{output}\""

        # run ffmpeg
        subprocess.run(command, shell=True)

        return f"Converted Successfully! Saved as: {output}"

    return render_template("index.html")


if __name__ == "__main__":
    app.run()
