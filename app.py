from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)
DOWNLOAD_FOLDER = os.path.join(os.getcwd(), "downloads")
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/download", methods=["POST"])
def download():
    url = request.form.get("url")
    if not url:
        return "URL tidak valid", 400
    # Simulasi: Download MP3 disini (bisa pakai yt_dlp kalau mau)
    return f"<h1>Download selesai!</h1><a href='#'>Unduh MP3</a>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
