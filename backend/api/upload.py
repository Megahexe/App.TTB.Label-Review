from pathlib import Path

from fastapi import APIRouter, UploadFile, File
from backend.services.image_service import get_file_info
from backend.services.ocr_service import extract_label_data

print("api/upload.py LOADED")

router = APIRouter()

UPLOAD_FOLDER = Path("uploads")
UPLOAD_FOLDER.mkdir(exist_ok=True)


@router.post("/upload")
async def upload_label(
    file: UploadFile = File(...)
):
    print("UPLOAD ENDPOINT CALLED")

    contents = await file.read()

    file_path = UPLOAD_FOLDER / file.filename

    with open(file_path, "wb") as f:
        f.write(contents)

    file_info = get_file_info(file_path)

    extraction = extract_label_data(file_path)

    return {
        "content_type": file.content_type,
        "saved_to": str(file_path),
        "file_info": file_info,
        "extraction": extraction
    }