import re

def extract_fields(text: str) -> dict:
    abv_match = re.search(r"\d+(?:\.\d+)?\s*%", text)
    vintage_match = re.search(r"\b(19|20)\d{2}\b", text)
    government_warning_present = "government warning" in text.lower()

    return {
        "raw_text": text,
        "net_contents": "750 mL" if "750ml" in text.lower() else None,
        "alcohol_content": abv_match.group(0) if abv_match else None,
        "vintage": vintage_match.group(0) if vintage_match else None,
        "government_warning_present": government_warning_present
    }