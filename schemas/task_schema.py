from pydantic import BaseModel, Field

class TaskSchema(BaseModel):
    title: str = Field(default=..., title="Title of the task")
    description: str = Field(default=..., title="Description of the task")

    class Config():
        orm_mode = True