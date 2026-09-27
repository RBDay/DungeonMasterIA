from datetime import datetime

from app.core.db import Base

from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column

import uuid
from sqlalchemy import Uuid

class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())