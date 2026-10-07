from backend.models.label_submission import LabelSubmission
from backend.models.label_extraction import LabelExtraction


def validate_label(
    submission: LabelSubmission,
    extraction: LabelExtraction
) -> dict:

    return {
        "brand_name_match":
            submission.brand_name.lower().strip()
            == extraction.brand_name.lower().strip(),

        "product_type_match":
            submission.product_type.lower().strip()
            == extraction.product_type.lower().strip(),

        "alcohol_content_match":
            submission.alcohol_content.lower().strip()
            == extraction.alcohol_content.lower().strip(),

        "government_warning_present":
            extraction.government_warning_present
    }