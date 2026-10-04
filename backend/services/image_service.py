from pathlib import Path

from PIL import Image


def get_file_info(file_path: Path) -> dict:
    extension = file_path.suffix.lower()

    try:
        with Image.open(file_path) as image:
            width, height = image.size
    except Exception:
        width = None
        height = None

    return {
        "filename": file_path.name,
        "extension": extension,
        "file_size_bytes": file_path.stat().st_size,
        "width": width,
        "height": height
    }