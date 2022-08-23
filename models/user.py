from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declared_attr
from sqlalchemy_imageattach.entity import Image, image_attachment

from database.base_model import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), index=True)
    full_name = Column(String(60), index=True)
    photo = image_attachment('userpicture')
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    # offline = Column(Boolean(), default=False)


class UserPicture(Base, Image):
    """User picture model."""

    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user = relationship('User')

    @declared_attr
    def url(self):
        return Column(String(255), default='media/user_default', nullable=False)