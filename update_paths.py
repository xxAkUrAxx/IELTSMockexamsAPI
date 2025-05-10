import os
import re

# Define the folder structure mapping
folder_mapping = {
    "ListeningTest1Section": "ListeningTest1/ListeningTest1Section",
    "ListeningTest1Results": "ListeningTest1/ListeningTest1Results",
    "ReadingTest1Section": "ReadingTest1/ReadingTest1Section",
    "ReadingTest1Results": "ReadingTest1/ReadingTest1Results",
    "WritingTest1task": "WritingTest1/WritingTest1task"
}

# File extensions to process
file_extensions = [".html", ".htm"]

# Walk through all files in the current directory and subdirectories
for root, dirs, files in os.walk("."):
    for file_name in files:
        if any(file_name.endswith(ext) for ext in file_extensions):
            file_path = os.path.join(root, file_name)
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            original_content = content

            # Update paths in the content based on the folder mapping
            for old_path, new_path in folder_mapping.items():
                content = re.sub(
                    rf'(["\']){old_path}(\d+\.html)\1',
                    rf'\1{new_path}\2\1',
                    content
                )

            # Only write back if content changed
            if content != original_content:
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(content)
                print(f"Updated paths in {file_path}")
