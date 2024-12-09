from sqlalchemy import select
from sqlalchemy.ext.asyncio import (
    AsyncSession, 
    async_sessionmaker
)
from sqlalchemy.exc import NoResultFound

from .models import Base, Book


async def insert_object(
        async_session: async_sessionmaker[AsyncSession],
        object: Base
        ) -> None:
    async with async_session() as session:
        async with session.begin():
            session.add(instance=object)
            await session.commit()


async def select_many(
        async_session: async_sessionmaker[AsyncSession],
        owner_id: int = None,
):
    async with async_session() as session:
        stmt = select(Book)
        if owner_id is not None:
            stmt = stmt.filter(Book.id == owner_id)
        stmt = stmt.order_by(Book.title)
        result = await session.execute(stmt)
        return result.scalars().all()
    

async def check_existence(
        async_session: async_sessionmaker[AsyncSession],
        model: Base,  # Модель, в которой будем проверять
        object_id: int
): # проверяет, существует ли объект по его ID
    async with async_session() as session:
        stmt = select(model).filter(model.id == object_id)
        result = await session.execute(stmt)
        return result.scalar() is not None
    

async def select_by_id(
        async_session: AsyncSession,
        model: Base,
        object_id: int
):
    async with async_session() as session:
        stmt = select(model).filter(model.id == object_id)
        result = await session.execute(stmt)
        return result.scalar()


async def delete_by_id(
        async_session: AsyncSession,
        model: Base,
        object_id: int
):
    async with async_session() as session:
        async with session.begin():
            stmt = select(model).filter(model.id == object_id)
            result = await session.execute(stmt)
            obj = result.scalar_one_or_none()
            
            if not obj:
                return
            
            await session.delete(obj)
            await session.commit()