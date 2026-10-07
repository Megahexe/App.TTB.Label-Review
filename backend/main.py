from fastapi import FastAPI

from backend.api.upload import router as upload_router
from models.label_submission import LabelSubmission
from services.ocr_service import extract_label_data
from validators.label_validator import validate_label
from models.application_data import ApplicationData
from services.comparison_service import compare_extractions

app = FastAPI(
    title="TTB Label Review API",
    version="0.1.0"
)

app.include_router(upload_router)

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

@app.post("/compare")
def compare(
    application_data: ApplicationData,
    extraction_data: dict
):
    return compare_extractions(
        application_data.model_dump(),
        extraction_data
    )