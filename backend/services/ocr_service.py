from pathlib import Path

import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files\Tesseract-OCR\tesseract.exe"

from models.label_extraction import LabelExtraction


def extract_label_data(file_path: Path | None = None) -> LabelExtraction:

    if file_path is not None:
        try:
            with Image.open(file_path) as image:
                text = pytesseract.image_to_string(image)

            print("\n====== OCR OUTPUT ======")
            print(text)
            print("========================\n")
            print(text)
            return {
                "raw_text": text,
                "net_contents": "750 mL" if "750ml" in text.lower() else None
            }

        except Exception as ex:
            print(f"OCR Error: {ex}")

    return LabelExtraction(
        brand_name="OLD TOM DISTILLERY",
        product_type="Kentucky Straight Bourbon Whiskey",
        alcohol_content="45%",
        net_contents="750 mL",
        government_warning_present=True
    )