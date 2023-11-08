import os
from datetime import datetime

from sqlalchemy import create_engine, String, DateTime, func, ForeignKey
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column

POSTGRES_USER = os.getenv('POSTGRES_USER', 'app')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', '123')
POSTGRES_DB = os.getenv('POSTGRES_DB', 'app')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', '127.0.0.1')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5431')

PG_DSN = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_engine(PG_DSN)
Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


# class Owners(Base):
#     __tablename__ = 'Owners'
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     email: Mapped[str] = mapped_column(String(100), nullable=False)
#     password: Mapped[int] = mapped_column(primary_key=True)
#
#     def dict(self):
#         return {
#             'id': self.id,
#             'name': self.email,
#             'password': self.password,
#         }


class ADS(Base):
    __tablename__ = 'app_ADS'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(1000), nullable=False)
    # date_of_creation: Mapped[datetime:datetime] = mapped_column(DateTime)
    # owner: Mapped[str] = mapped_column(ForeignKey(Owners.id))
    owner: Mapped[str] = mapped_column(String(100), nullable=False)

    @property
    def dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            # 'date_of_creation': self.date_of_creation.isoformat,
            'owner': self.owner
        }


Base.metadata.create_all(bind=engine)
