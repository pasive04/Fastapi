from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime

class Appointment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    date: datetime = Field(default_factory=datetime.now)
    title: str
    description: Optional[str] = None
    

