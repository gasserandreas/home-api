# Home API Service

A FastAPI-based REST API service that interfaces with a PostgreSQL database.

## Prerequisites

- Python 3.9 or higher
- PostgreSQL database
- uv (optional, but recommended)

## Setup

### 1. Set up environment

Create a `.env` file in the root directory from .env.example: `cp .env.example .env` and update variables with Postgres credentials 

### 2. Install dependencies

Active environment and install dependencies using uv (recommended):
```
source ./.venv/bin/activate
uv pip install -r requirements.txt
```

### 3. Start the application

Run the FastAPI application:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`. You can access the interactive API documentation at `http://localhost:8000/docs`.
