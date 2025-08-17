import os
import shutil
import sys

# Categories and their extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Programs": [".py", ".java", ".c", ".cpp", ".js", ".html", ".css"],
}

def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"❌ Folder not found: {folder_path}")
        return

    print(f"📂 Organizing folder: {folder_path}")

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False

            # Check category and move file
            for category, extensions in FILE_CATEGORIES.items():
                if file_ext in extensions:
                    category_folder = os.path.join(folder_path, category)
                    os.makedirs(category_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(category_folder, filename))
                    moved = True
                    break

            # If extension not found → move to Others
            if not moved:
                other_folder = os.path.join(folder_path, "Others")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, filename))

    print("✅ Done! Files have been organized.")

if __name__ == "__main__":
    # If user dragged a folder onto Automator or script was run with argument
    if len(sys.argv) > 1:
        folder_to_organize = sys.argv[1]
    else:
        # Ask user if no folder was given
        folder_to_organize = input("Enter the path of the folder to organize: ")

    organize_folder(folder_to_organize)
