from pathlib import Path

from fastapi import APIRouter, UploadFile, File

router = APIRouter()

UPLOAD_FOLDER = Path("uploads")
UPLOAD_FOLDER.mkdir(exist_ok=True)


@router.post("/upload")
async def upload_label(
    file: UploadFile = File(...)
):
    contents = await file.read()

    file_path = UPLOAD_FOLDER / file.filename

    with open(file_path, "wb") as f:
        f.write(contents)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "file_size_bytes": len(contents),
        "saved_to": str(file_path)
    }