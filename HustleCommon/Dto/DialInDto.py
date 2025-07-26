from pydantic import BaseModel
from typing import List, Optional

class DialInDto(BaseModel):
    beansName: Optional[str] = None
    roastDate: Optional[str] = None
    dialedBy: Optional[List[str]] = None
    dose: Optional[float] = None
    time: Optional[float] = None
    calibrationYield: Optional[float] = None
    sweetSpot: Optional[float] = None
    tools: Optional[List[str]] = None
    grindSize: Optional[float] = None
    mouthFeel: Optional[str] = None
    black: Optional[str] = None
    espressoNotes: Optional[str] = None
    americanoNotes: Optional[str] = None
    white: Optional[str] = None
    cappuccinoNotes: Optional[str] = None
    latteNotes: Optional[str] = None
