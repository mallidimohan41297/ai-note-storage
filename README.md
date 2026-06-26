# AI-Powered Student Notes Storage System on AWS

A production-quality, modular cloud application designed to securely manage academic resources using Python, Flask, and Amazon Web Services (AWS) S3. This project demonstrates enterprise software engineering principles, robust cloud infrastructure integration, and structured exception handling.

## 🚀 Key Features
* **Secure Cloud Uploads:** Uploads academic resources (`.pdf`, `.docx`, `.pptx`, images) directly to AWS S3 with automated MIME-type detection.
* **Granular Metadata Listing:** Fetches real-time bucket contents including exact file sizes (KB) and human-readable upload timestamps.
* **Secure File Retrieval:** Generates time-bound, secure S3 presigned URLs for safe data downloading without exposing public bucket access.
* **Safe Cloud Deletion:** Clean removal of specific object keys from AWS storage with explicit UI confirmation guards.
* **Live Search Filter:** Instant frontend scanning across stored resources optimized to reduce API retrieval latency.
* **Responsive Dashboard:** A clean user interface built using **Bootstrap 5**, fully responsive across mobile and desktop viewports.

---

## 🏗️ Architecture & Component Design

The system implements a decoupled **3-Tier Web Architecture**:
1. **Presentation Layer (Frontend):** HTML5, CSS3, Bootstrap 5 UI.
2. **Application Layer (Backend Engine):** Python 3.12+ and Flask handling routing, validation, and session contexts.
3. **Data Storage Layer (Cloud Infrastructure):** AWS S3 via the official Boto3 SDK.

```text
ai_notes_storage/
│
├── src/                        # Main source code directory
│   ├── app.py                  # Routing engine & entry point
│   ├── config.py               # Environment configuration manager
│   ├── s3_manager.py           # Core cloud infrastructure logic (Boto3 API)
│   └── templates/
│       └── index.html          # Responsive Bootstrap 5 Dashboard
│
├── .env                        # Local infrastructure secrets (Git ignored)
├── .gitignore                  # Tracking isolation matrix
└── requirements.txt            # Explicit dependency manifest with pinned versions
