from pathlib import Path

import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files\Tesseract-OCR\tesseract.exe"

from services.extraction_service import extract_fields


def extract_label_data(file_path: Path | None = None) -> dict:

    if file_path is not None:
        try:
            with Image.open(file_path) as image:
                text = pytesseract.image_to_string(image)

            print("\n====== OCR OUTPUT ======")
            print(text)
            print("========================\n")

            return extract_fields(text)

        except Exception as ex:
            print(f"OCR Error: {ex}")
