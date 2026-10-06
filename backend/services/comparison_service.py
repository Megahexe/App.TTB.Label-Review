def compare_fields(
    application_value,
    label_value
) -> str:

    if label_value is None:
        return "MISSING"

    if application_value == label_value:
        return "MATCH"

    return "MISMATCH"

def compare_extractions(
    application_data: dict,
    extraction_data: dict
) -> dict:

    return {
        "alcohol_content": compare_fields(
            application_data.get("alcohol_content"),
            extraction_data.get("alcohol_content")
        ),
        "net_contents": compare_fields(
            application_data.get("net_contents"),
            extraction_data.get("net_contents")
        ),
        "vintage": compare_fields(
            application_data.get("vintage"),
            extraction_data.get("vintage")
        ),
        "government_warning_present": compare_fields(
            application_data.get("government_warning_present"),
            extraction_data.get("government_warning_present")
        )
    }