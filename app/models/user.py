from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime, timezone

class User(SQLModel, table=True):
	id: Optional[int] = Field(default=None, primary_key=True)
	name: str
	email: str
	password_hash: str
	role: str # "customer", "restaurant_owner", or "admin"
	created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
	updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
	