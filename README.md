# Pincode Lookup

A small FastAPI service for looking up Indian pincodes.

## Setup

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

The API is available at `http://127.0.0.1:8000`. Interactive docs are at `/docs`.

## Endpoints

- `GET /pincode/{code}` - Look up one six-digit pincode.
- `POST /pincode/bulk` - Look up multiple pincodes.

Example request:

```json
{"codes": ["110001", "400001"]}
```