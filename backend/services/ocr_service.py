from models.label_extraction import LabelExtraction


def extract_label_data() -> LabelExtraction:
    """
    Placeholder OCR service.

    Later this will call:
    - Azure Document Intelligence
    - Tesseract
    - Other OCR providers

    For now, return sample data.
    """

    return LabelExtraction(
        brand_name="OLD TOM DISTILLERY",
        product_type="Kentucky Straight Bourbon Whiskey",
        alcohol_content="45%",
        net_contents="750 mL",
        government_warning_present=True
    )