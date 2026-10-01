from fastapi import Request
from fastapi.responses import JSONResponse


class PincodeNotFoundError(Exception):
    def __init__(self, pincode: str) -> None:
        self.pincode = pincode


class InvalidPincodeError(Exception):
    def __init__(self, pincode: str, reason: str = "Invalid Pincode") -> None:
        self.pincode = pincode
        self.reason = reason


# Exeption Handlers


async def pincode_not_found_exception(req: Request, exc: PincodeNotFoundError):
    return JSONResponse(
        status_code=404,
        content={
            "error": "pincode_not_found",
            "message": f"pincode: {exc.pincode} was not found",
        },
    )

async def invalid_pincode_exception(req: Request, exc: InvalidPincodeError):
    return JSONResponse(
        status_code=400,
        content={
            "error": "invalid_pincode_error",
            "message": f"pincode: {exc.pincode} is not valid",
        },
    )