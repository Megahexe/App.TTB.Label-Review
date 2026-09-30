\# Architecture



\## Overview



The application consists of two primary components:



1\. Frontend (Next.js)

2\. Backend API (FastAPI)



\## User Workflow



1\. User uploads a label image.

2\. Backend receives the image.

3\. OCR extracts text.

4\. Validation engine analyzes extracted data.

5\. Results are returned to the frontend.

6\. User reviews findings.



\## Components



\### Frontend



Responsibilities:



\- Upload labels

\- Display results

\- Batch processing interface



\### Backend



Responsibilities:



\- File handling

\- OCR processing

\- Validation logic

\- Report generation



\### OCR Layer



Responsibilities:



\- Extract text from label images

\- Handle imperfect image quality where possible



\### Validation Engine



Checks:



\- Brand name

\- Alcohol content

\- Class/type designation

\- Net contents

\- Government warning statement



\## Design Constraints



\- Standalone proof of concept

\- No direct COLA integration

\- No runtime dependency on TTB.gov

\- Simple user interface

\- Fast response time target (<5 seconds)

