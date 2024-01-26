from sqlalchemy import Table, Column, MetaData, Integer, Computed, VARCHAR, text, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from typing import Annotated
from datetime import datetime


intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]
date_create = Annotated[datetime, mapped_column(server_default=text('CURRENT_TIMESTAMP()'))]
varchar_255 = Annotated[str, mapped_column(type_=VARCHAR(255))]
varchar_50 = Annotated[str, mapped_column(type_=VARCHAR(50))]
varchar_1000 = Annotated[str, mapped_column(type_=VARCHAR(1000))]


class Base(DeclarativeBase):
    __table_args__= {"schema":"fastapi_auth"}
