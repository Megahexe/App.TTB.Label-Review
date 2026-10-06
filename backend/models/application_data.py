from pydantic import BaseModel


class ApplicationData(BaseModel):
    alcohol_content: str | None = None
    net_contents: str | None = None
    vintage: str | None = None
    government_warning_present: bool | None = None