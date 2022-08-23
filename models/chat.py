from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Text, func, DateTime
from sqlalchemy.orm import relationship

from database.base_model import Base


class Chat(Base):
    id = Column(Integer, primary_key=True, index=True)
    # chat_id = Column(Integer, ForeignKey('chat.id'), nullable=False)
    title = Column(String(255), nullable=False)
    owner = Column(Integer, ForeignKey('user.id'), nullable=False)
