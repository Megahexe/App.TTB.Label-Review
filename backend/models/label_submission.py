from pydantic import BaseModel


class LabelSubmission(BaseModel):
    brand_name: str
    product_type: str
    alcohol_content: str
