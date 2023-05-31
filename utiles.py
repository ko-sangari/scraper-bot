from pydantic import BaseModel
from typing import List


class City(BaseModel):
    id: int
    name: str
    clients: List[int] = []
