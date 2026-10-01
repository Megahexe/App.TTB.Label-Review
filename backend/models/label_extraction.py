from pydantic import BaseModel


class LabelExtraction(BaseModel):
    brand_name: str | None = None
    product_type: str | None = None
    alcohol_content: str | None = None
    net_contents: str | None = None
    government_warning_present: bool = False