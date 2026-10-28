
from flask import Flask, render_template
import os
import shutil

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_FOLDER = os.path.join(BASE_DIR, "TestFiles")

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".doc"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"],
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/organize", methods=["POST"])
def organize():
    messages = []

    if not os.path.isdir(TEST_FOLDER):
        return render_template(
            "index.html",
            messages=["TestFiles folder was not found."]
        )

    for file_name in os.listdir(TEST_FOLDER):
        source = os.path.join(TEST_FOLDER, file_name)

        if not os.path.isfile(source):
            continue

        extension = os.path.splitext(file_name)[1].lower()
        category = "Other Files"

        for folder_name, extensions in FILE_TYPES.items():
            if extension in extensions:
                category = folder_name
                break

        destination_folder = os.path.join(TEST_FOLDER, category)
        os.makedirs(destination_folder, exist_ok=True)

        destination = os.path.join(destination_folder, file_name)

        if os.path.exists(destination):
            messages.append(f"Skipped duplicate: {file_name}")
            continue

        shutil.move(source, destination)
        messages.append(f"Moved {file_name} to {category}")

    messages.append("File organization completed!")

    return render_template("index.html", messages=messages)


if __name__ == "__main__":
    app.run(debug=True)
