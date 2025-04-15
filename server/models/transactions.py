
from server.models import Base, TimestampMixin
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String,Boolean,Integer


class Transaction(Base,TimestampMixin):
    __tablename__ ='Transactions'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    table:Mapped[str] = mapped_column(String) 
    transaction:Mapped[str] = mapped_column(String)    
    status: Mapped [str] = mapped_column(String)