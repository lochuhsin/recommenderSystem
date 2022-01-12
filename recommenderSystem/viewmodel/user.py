from typing import Optional, List
from pydantic import BaseModel

class user_info(BaseModel):
	user_id: str


class user_data(BaseModel):
	users: List[user_info]
	method: str