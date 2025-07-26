from pydantic import BaseModel
from typing import List, Optional

class DialInModel(BaseModel):
    guid: str = None
    beansName: str = None
    date: str = None
    roastDate : str = None
    dialedBy: Optional[List[str]] = None
    dose: float = None
    time: float = None
    calibrationYield: float = None
    sweetSpot: float = None
    tools: Optional[List[str]] = None
    grindSize: float = None
    mouthFeel: str = None
    black: str = None
    espressoNotes: str = None
    americanoNotes: str = None
    white: str = None
    cappuccinoNotes: str = None
    latteNotes: str = None
    updatedAt: str = None

