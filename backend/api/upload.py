from fastapi import APIRouter, UploadFile, File

router = APIRouter()


@router.post("/upload")
async def upload_label(
    file: UploadFile = File(...)
):
    contents = await file.read()

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "file_size_bytes": len(contents)
    }