from pydantic import BaseModel, Field

class UserSchema(BaseModel):
    name: str = Field(default=..., title="Name of the user")
    email: str = Field(default=..., title="Email of the user")
    password: str = Field(default=..., title="Password of the user")

    class Config():
        orm_mode = True