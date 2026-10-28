
import os
import shutil

def organize_files(folder_path):
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt", ".doc"],
        "Videos": [".mp4", ".mkv", ".avi"],
        "Audio": [".mp3", ".wav"],
    }

    if not os.path.isdir(folder_path):
        print("Folder not found!")
        return

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if not os.path.isfile(file_path):
            continue

        extension = os.path.splitext(file_name)[1].lower()
        category = "Other Files"

        for folder_name, extensions in file_types.items():
            if extension in extensions:
                category = folder_name
                break

        destination_folder = os.path.join(folder_path, category)
        os.makedirs(destination_folder, exist_ok=True)
        destination_path = os.path.join(destination_folder, file_name)

        if os.path.exists(destination_path):
            print(f"Skipped duplicate file: {file_name}")
            continue

        shutil.move(file_path, destination_path)
        print(f"Moved {file_name} to {category}")

    print("File organization completed!")


if __name__ == "__main__":
    test_folder = os.path.join(os.path.dirname(__file__), "TestFiles")
    organize_files(test_folder)