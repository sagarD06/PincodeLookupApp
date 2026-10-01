from pydantic import BaseModel, field_validator


class PincodeRequest(BaseModel):
    code: str

    @field_validator("code")
    @classmethod
    def validate_code(cls, value):
        if len(value) != 6 or not value.isdigit():
            raise ValueError("Pincode must be exactly 6 digits")
        return value


class LocationResponse(BaseModel):
    pincode: str
    city: str
    state: str
    district: str


class BulkRequest(BaseModel):
    codes: list[str]

    @field_validator("codes")
    @classmethod
    def validate_codes(cls, values):
        if not values:
            raise ValueError("Atleast 1 pincode is expected")

        for code in values:
            if len(code) != 6 or not code.isdigit():
                raise ValueError("Each Pincode must be exactly 6 digits")
        return values


class BulkResponse(BaseModel):
    status: str = "success"
    found: int
    not_found: int
    results: list[LocationResponse]
    missing: list[str]
