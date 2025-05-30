from dataclasses import dataclass
from typing import List


@dataclass
class BusinessModel:
    ingredient : List[int]
    expectedProfit: int