import os
from pathlib import Path
import shutil

directory_path = Path("c:/Users/HP/Downloads")
for entry in directory_path.iterdir():
    if entry.is_file():
        extension = entry.suffix[1:].lower()
        destination_folder = None
        
        if extension in ["pdf", "docx", "txt", "xlsx"]:
            destination_folder = "c:/Users/HP/Downloads/Documents"
        elif extension in ["jpg", "png", "gif", "svg"]:
            destination_folder = "c:/Users/HP/Downloads/Images"
        elif extension in ["mp4", "mov", "avi"]:
            destination_folder = "c:/Users/HP/Downloads/Videos"
        elif extension in ["mp3", "wav", "flac"]:
            destination_folder = "c:/Users/HP/Downloads/Audio"
        elif extension in ["zip", "rar", "tar", "gz"]:
            destination_folder = "c:/Users/HP/Downloads/Archives"
        elif extension in ["py", "js", "html", "css"]:
            destination_folder = "c:/Users/HP/Downloads/Code"
        else:
            destination_folder = "c:/Users/HP/Downloads/Others"

        if destination_folder:
            destination = Path(destination_folder) / entry.name
            
            if destination.exists():
                print(f"Skipped {entry.name} - already exists")
            else:
                shutil.move(str(entry), str(destination))
                print(f"Moved {entry.name}")
                