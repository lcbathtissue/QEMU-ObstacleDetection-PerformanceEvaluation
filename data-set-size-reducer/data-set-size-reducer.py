import shutil
import os

def list_nth_files(directory, n):
    file_count = 0

    if not os.path.exists(directory) or not os.path.isdir(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    for filename in sorted(os.listdir(directory)):
        if filename.startswith("frame_") and filename.endswith(".jpg"):
            if file_count % n == 0:
                source_file = os.path.join(directory, filename) 
                copy_file_to_reduced_directory(source_file, directory)
            file_count += 1

def copy_file_to_reduced_directory(source_file, directory):
    if not os.path.exists(f"{directory}_reduced"):
        os.makedirs(f"{directory}_reduced")

    base_name = os.path.basename(source_file)
    reduced_file = os.path.join(f"{directory}_reduced", base_name.replace(".jpg", "_reduced.jpg"))

    shutil.copy(source_file, reduced_file)

if __name__ == "__main__":
    directory = input("Enter the directory path: ")
    n = int(input("Enter N (every N images will be saved): "))

    list_nth_files(directory, n)
