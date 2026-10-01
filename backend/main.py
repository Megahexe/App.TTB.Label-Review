from fastapi import FastAPI

from models.label_submission import LabelSubmission
from services.ocr_service import extract_label_data
from validators.label_validator import validate_label

app = FastAPI(
    title="TTB Label Review API",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "TTB Label Review API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/analyze")
def analyze_label(submission: LabelSubmission):

    extraction = extract_label_data()

    results = validate_label(
        submission=submission,
        extraction=extraction
    )

    return {
        "submission": submission,
        "extraction": extraction,
        "results": results
    }