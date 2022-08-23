from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Text, func, DateTime
from sqlalchemy.orm import relationship

from database.base_model import Base


class Message(Base):
    id = Column(Integer, primary_key=True, index=True)
    from_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    # chat_id = Column(Integer, ForeignKey('chat.id'), nullable=False)
    reply_to = Column(Integer, ForeignKey('user.id'), nullable=True)
    message = Column(Text, nullable=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_modified = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.current_timestamp())
