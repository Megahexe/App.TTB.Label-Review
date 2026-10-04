from pathlib import Path

from models.label_extraction import LabelExtraction


def extract_label_data(file_path: Path | None = None) -> LabelExtraction:
    """
    Placeholder OCR service.

    In a future version:
    - Load image
    - Run OCR
    - Extract label fields

    For now, return sample data.
    """

    return LabelExtraction(
        brand_name="OLD TOM DISTILLERY",
        product_type="Kentucky Straight Bourbon Whiskey",
        alcohol_content="45%",
        net_contents="750 mL",
        government_warning_present=True
    )