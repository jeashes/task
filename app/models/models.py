from pydantic import BaseModel, Field

class MessageData(BaseModel):
    message: str = Field(...)
