import os
from reviewFile import evaluateCodeFile



def traverse_directory(path, ignore_folders=[], ignore_files=[]):
    for root, dirs, files in os.walk(path):
        # Exclude specified folders
        dirs[:] = [d for d in dirs if d not in ignore_folders]

        for file in files:
            if file not in ignore_files:
                file_path = os.path.join(root, file)
                evaluateCodeFile(file_path)


def __init__():
    path = input("Enter the path of the directory: ")
    traverse_directory(path, ignore_folders=[".git", "venv", "node_modules", ".conda", "__pycache__"], ignore_files=[".DS_Store", "Thumbs.db"])

__init__()