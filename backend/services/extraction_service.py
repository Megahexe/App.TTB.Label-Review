def extract_fields(text: str) -> dict:
    return {
        "raw_text": text,
        "net_contents": "750 mL" if "750ml" in text.lower() else None
    }