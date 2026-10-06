import re

def extract_fields(text: str) -> dict:
    abv_match = re.search(r"\d+(?:\.\d+)?\s*%", text)

    return {
        "raw_text": text,
        "net_contents": "750 mL" if "750ml" in text.lower() else None,
        "alcohol_content": abv_match.group(0) if abv_match else None
    }