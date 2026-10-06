# App.TTB.Label-Review

AI-powered alcohol beverage label review and compliance validation tool for TTB application workflows.

---

# Overview

App.TTB.Label-Review is a proof-of-concept application designed to assist beverage label reviewers by automating portions of the label review process.

The system uses Optical Character Recognition (OCR) to extract text from uploaded beverage label images, identifies key label information, and compares that information against submitted application data.

The goal is to demonstrate how OCR and automated validation can reduce manual review effort and help identify discrepancies between label content and application submissions.

---

# Problem Statement

Reviewing alcohol beverage labels is a time-consuming process that requires reviewers to manually inspect labels and compare them against submitted application data.

Common challenges include:

- Verifying alcohol content
- Verifying net contents
- Confirming vintage information
- Identifying required warning statements
- Detecting missing or incorrect information
- Comparing label information against application data

This project explores how OCR and automated rule-based validation can assist reviewers by rapidly identifying key information and highlighting potential issues.

---

# Features

## OCR-Based Text Extraction

The application uses Tesseract OCR to extract text from uploaded label images.

Supported file formats:

- PNG
- JPG
- JPEG

Example OCR Output:

```text
JACKSE
ESERVE

2012

Estate Bottled

CABERNET SAUVIGNON

Jackse Estate Vineyard
ST. HELENA + NAPA VALLEY

Alc. 14.1% by Vol
```

---

## Label Field Extraction

The system currently extracts the following core fields:

### Alcohol Content

Example:

```text
Alc. 14.1% by Vol
```

Extracted value:

```json
{
  "alcohol_content": "14.1%"
}
```

### Net Contents

Example:

```text
750ml
```

Extracted value:

```json
{
  "net_contents": "750 mL"
}
```

### Vintage

Example:

```text
2012
```

Extracted value:

```json
{
  "vintage": "2012"
}
```

### Government Warning Detection

The application checks whether OCR text contains a Government Warning statement.

Example output:

```json
{
  "government_warning_present": true
}
```

or

```json
{
  "government_warning_present": false
}
```

---

## Label Comparison Engine

The application compares extracted label information against application data.

Comparison results include:

- MATCH
- MISMATCH
- MISSING

Example:

```json
{
  "alcohol_content": "MATCH",
  "net_contents": "MISSING",
  "vintage": "MATCH"
}
```

---

## Review Summary

The comparison engine generates a summary of review results.

Example:

```json
{
  "summary": {
    "matches": 3,
    "mismatches": 0,
    "missing": 1
  }
}
```

---

# System Architecture

```text
Label Image
     │
     ▼
OCR Service
(Tesseract)
     │
     ▼
Raw OCR Text
     │
     ▼
Extraction Service
     │
     ▼
Structured Fields
     │
     ▼
Comparison Service
     │
     ▼
Review Results
```

---

# Repository Structure

```text
App.TTB.Label-Review/
│
├── backend/
│   ├── api/
│   ├── models/
│   ├── services/
│   │   ├── ocr_service.py
│   │   ├── extraction_service.py
│   │   └── comparison_service.py
│   ├── uploads/
│   ├── requirements.txt
│   └── main.py
│
├── frontend/
│
├── docs/
│
└── README.md
```

---

# Technology Stack

## Backend

- Python
- FastAPI
- Pydantic

## OCR

- Tesseract OCR
- pytesseract
- Pillow

## Development Tools

- Git
- GitHub
- GitHub Desktop

---

# Prerequisites

Before running the application, install:

- Python
- Tesseract OCR

Tesseract OCR is required because it is not installed through `requirements.txt`.

After installing Tesseract, verify the installation:

```powershell
tesseract --version
```

Expected output:

```text
tesseract v5.x.x
```

If the command is not recognized, ensure the Tesseract installation directory has been added to the system PATH and restart PowerShell.

---

# Installation

## Clone Repository

```powershell
git clone <repository-url>
```

## Navigate to Backend

```powershell
cd backend
```

## Create Virtual Environment

```powershell
python -m venv .venv
```

## Activate Virtual Environment

```powershell
.\.venv\Scripts\Activate.ps1
```

## Install Dependencies

```powershell
pip install -r requirements.txt
```

---

# Running the Application

Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Start FastAPI:

```powershell
uvicorn main:app --reload
```

Expected output:

```text
INFO:     Application startup complete.
```

---

# API Documentation

After starting the application, open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI provides interactive API documentation and testing.

---

# API Endpoints

## POST /upload

Uploads a label image, performs OCR, and extracts core label fields.

### Request

Multipart file upload.

Supported formats:

- PNG
- JPG
- JPEG

### Example Response

```json
{
  "content_type": "image/jpeg",
  "saved_to": "uploads\\example.jpg",
  "file_info": {
    "filename": "example.jpg",
    "extension": ".jpg",
    "file_size_bytes": 179875,
    "width": 1274,
    "height": 725
  },
  "extraction": {
    "raw_text": "...",
    "net_contents": "750 mL",
    "alcohol_content": "14.1%",
    "vintage": "2012",
    "government_warning_present": false
  }
}
```

---

## POST /compare

Compares extracted label data against application data.

### Example Request

```json
{
  "application_data": {
    "alcohol_content": "14.1%",
    "net_contents": "750 mL",
    "vintage": "2012",
    "government_warning_present": false
  },
  "extraction_data": {
    "alcohol_content": "14.1%",
    "net_contents": "750 mL",
    "vintage": "2012",
    "government_warning_present": false
  }
}
```

### Example Response

```json
{
  "summary": {
    "matches": 4,
    "mismatches": 0,
    "missing": 0
  },
  "results": {
    "alcohol_content": "MATCH",
    "net_contents": "MATCH",
    "vintage": "MATCH",
    "government_warning_present": "MATCH"
  }
}
```

---

# Example Workflow

## Step 1

Upload a beverage label image using:

```text
POST /upload
```

## Step 2

OCR extracts text from the image.

Example:

```text
Alc. 14.1% by Vol
```

## Step 3

The extraction service identifies label fields.

Example:

```json
{
  "alcohol_content": "14.1%",
  "vintage": "2012"
}
```

## Step 4

Submit application data using:

```text
POST /compare
```

## Step 5

Review comparison results.

Example:

```json
{
  "summary": {
    "matches": 3,
    "mismatches": 0,
    "missing": 1
  }
}
```

---

# Current Limitations

This project is a proof-of-concept.

Known limitations include:

- OCR accuracy depends on image quality
- Limited extraction fields
- Simple rule-based matching
- No direct integration with TTB systems
- No authentication or authorization
- No batch processing implementation
- No confidence scoring

---

# Assumptions

- This project is a standalone proof-of-concept.
- The application operates independently of TTB production systems.
- Validation rules are simplified for demonstration purposes.
- OCR results may vary depending on image quality.

---

# Future Enhancements

Potential future enhancements include:

- Additional field extraction
- Brand and product identification
- Enhanced government warning validation
- OCR image preprocessing
- Batch processing support
- Reviewer workflow enhancements
- User interface improvements
- Expanded comparison and validation rules

---

# Project Status

Current Status:

✅ OCR Integration Complete

✅ Label Upload Workflow Complete

✅ Core Field Extraction Complete

✅ Label Comparison Engine Complete

✅ Review Summary Generation Complete

✅ End-to-End Proof of Concept Functional

The project successfully demonstrates the complete workflow:

```text
Label Upload
     ↓
OCR Processing
     ↓
Field Extraction
     ↓
Comparison Against Application Data
     ↓
Review Results
```