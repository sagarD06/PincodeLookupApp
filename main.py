from fastapi import FastAPI

from data import pincode_db
from exceptions import (
    InvalidPincodeError,
    PincodeNotFoundError,
    invalid_pincode_exception,
    pincode_not_found_exception,
)
from models import BulkRequest, BulkResponse, LocationResponse

app = FastAPI(
    title="Pincode Lookup", description="Backend fopr looking up valid pincodes"
)

app.add_exception_handler(PincodeNotFoundError, pincode_not_found_exception)  # type: ignore[arg-type]
app.add_exception_handler(InvalidPincodeError, invalid_pincode_exception)  # type: ignore[arg-type]


@app.get("/")
def root():
    return {"message": "Welcome to pincode look up!"}


@app.get("/pincode/{code}", response_model=LocationResponse)
def get_pincode(code: str):
    if len(code) != 6 or not code.isdigit():
        raise InvalidPincodeError(pincode=code, reason="Invalid pincode")

    if code not in pincode_db:
        raise PincodeNotFoundError(pincode=code)

    return pincode_db[code]


@app.post("/pincode/bulk", response_model=BulkResponse)
def get_bulk_codes(req: BulkRequest):
    results = []
    missing = []
    for code in req.codes:
        if code in pincode_db:
            results.append(pincode_db[code])
        else:
            missing.append(code)

    return BulkResponse(
        found=len(results), not_found=len(missing), results=results, missing=missing
    )
