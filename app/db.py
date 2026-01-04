from collections.abc import AsyncGenerator
import datetime
import time
import uuid
from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, relationship
from datetime import datetime

# Database link
DATABASE_URL = "sqlite+aiosqlite:///./test.db"

# Data model for the data to be stored
class Base(DeclarativeBase):
    pass

class Post(Base):
    __tablename__ = "posts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    caption = Column(Text)
    url = Column(String, nullable=False)
    file_type = Column(String, nullable=False)
    file_name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

# creation of database
engine = create_async_engine(DATABASE_URL)

# creation of asynchronus sessions
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

# code to create the database and the tables
async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# to create an asnychronus session to perform operations over the data
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
