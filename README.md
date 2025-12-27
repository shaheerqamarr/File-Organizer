# Downloads Folder Organizer

A Python script that automatically organizes your Downloads folder by sorting files into categorized subfolders based on their file extensions.

## Features

- Automatically sorts files into categories (Documents, Images, Videos, Audio, Archives, Code, Others)
- Handles duplicate files by skipping them
- Creates category folders automatically if they don't exist
- Provides console feedback on which files were moved or skipped

## Categories

The script organizes files into the following categories:

- **Documents**: pdf, docx, txt, xlsx
- **Images**: jpg, png, gif, svg
- **Videos**: mp4, mov, avi
- **Audio**: mp3, wav, flac
- **Archives**: zip, rar, tar, gz
- **Code**: py, js, html, css
- **Others**: All other file types

## Requirements

- Python 3.6 or higher
- No external libraries required (uses built-in modules: `os`, `pathlib`, `shutil`)

## Installation

1. Clone or download this repository
2. No additional installation needed - uses Python standard library only

## Usage

1. Update the `directory_path` variable in the script to match your Downloads folder location:
```python
   directory_path = Path("c:/Users/YourUsername/Downloads")
```

2. Run the script:
```bash
   python organize_downloads.py
```

3. The script will:
   - Scan all files in your Downloads folder
   - Create category folders if they don't exist
   - Move files to their appropriate category folders
   - Print status messages for each file

## Example Output
```
Moved report.pdf
Moved photo.jpg
Skipped document.docx - already exists
Moved song.mp3
Moved script.py
```

## Customization

### Adding New File Extensions

To add support for more file types, edit the extension lists:
```python
if extension in ["pdf", "docx", "txt", "xlsx", "pptx"]:  # Added pptx
    destination_folder = "c:/Users/HP/Downloads/Documents"
```

### Adding New Categories

Add a new elif block for your custom category:
```python
elif extension in ["exe", "msi", "dmg"]:
    destination_folder = "c:/Users/HP/Downloads/Installers"
```

### Handling Duplicates

The current version skips files that already exist in the destination. To change this behavior:

**Auto-rename duplicates:**
```python
if destination.exists():
    counter = 1
    stem = entry.stem
    suffix = entry.suffix
    
    while destination.exists():
        new_name = f"{stem}_{counter}{suffix}"
        destination = Path(destination_folder) / new_name
        counter += 1

shutil.move(str(entry), str(destination))
```

## Safety Notes

- The script **moves** files (not copies), so files are removed from the main Downloads folder
- Files with duplicate names are skipped by default to prevent data loss
- The script only processes files, not folders
- Test on a backup folder first if you're concerned about your files

## Future Improvements

- [ ] Add command-line arguments for custom folder paths
- [ ] Support for organizing by date
- [ ] GUI interface
- [ ] Undo functionality
- [ ] Configuration file for custom categories
- [ ] Scheduling/automation (run on startup or periodically)

## License

This project is free to use and modify for personal or commercial purposes.

## Contributing

Feel free to fork this project and submit pull requests with improvements!

## Author

Created as a simple utility for keeping Downloads folders organized.
