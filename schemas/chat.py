from pydantic import BaseModel


class ChatBase(BaseModel):
    id: int | None = None
    title: str | None = None
    owner: int | None = None

    class Config:
        orm_mode = True


class ChatCreate(MessageBase):
    title: str
    owner: str


class MessageUpdate(MessageBase):
    id: int
    title: str
