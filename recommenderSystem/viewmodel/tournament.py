from typing import Optional, List
from pydantic import BaseModel


class tournament_info(BaseModel):
	sportid: int = 0
	tournamentid: int = 0
	date: str  # prematch 'xxxx-xx-xx xx:xx:xx', live 'seconds'

class tournament_data(BaseModel):
	data: List[tournament_info]

class tournament_rank(BaseModel):
	data: List[float]







