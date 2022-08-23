from datetime import datetime

from pydantic import BaseModel, EmailStr


class MessageBase(BaseModel):
    id: int | None = None
    from_id: int | None = None
    chat_id: int | None = None
    reply_to: int | None = None
    message: str | None = None
    time_created: datetime | None = None
    time_modified: datetime | None = None

    class Config:
        orm_mode = True


class MessageCreate(MessageBase):
    message: str


class MessageUpdate(MessageBase):
    id: int
    message: str
