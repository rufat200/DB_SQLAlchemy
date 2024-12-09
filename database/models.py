from sqlalchemy import ForeignKey
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column
    )

class Base(AsyncAttrs, DeclarativeBase):
    pass

class Book(Base):
    __tablename__ = "book"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("author.id"))
    genre_id: Mapped[int] = mapped_column(ForeignKey("genre.id"))

class Author(Base):
    __tablename__ = "author"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]

class Genre(Base):
    __tablename__ = "genre"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]