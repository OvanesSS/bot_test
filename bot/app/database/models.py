from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
	pass


class User(Base):
	__tabletname__ = 'users'

	id: Mapped[int] = mapped_column(primary_key=True)
	td_id: mapped_column(BigInteger)


class Category(Base):
	__tabletname__='categories'

	id: Mapped[int] = mapped_column(primary_key=True)
	name: Mapped[str] = mapped_column(String(25))


class Item(Base):
	__tabletname__ = 'items'

	id: Mapped[int] = mapped_column(primary_key=True)
	name: Mapped[str] = mapped_column(String(25))
	description: Mapped[str] = mapped_column(String(120))
	price: Mapped[int] = mapped_column()
	category: Mapped[int] = mapped_column(ForeignKey('categories.id'))


async def async_main():
	async with engine.begin() as conn:
		await conn.run_sync(Base.metadata.create_all)