from pydantic import BaseModel, EmailStr


class RegisterUser(BaseModel):
    first_name: str
    last_name: str
    email_address: EmailStr
    mobile_number: str
    password: str


class LoginUser(BaseModel):
    email_address: EmailStr | None = None
    mobile_number: str
    password: str
