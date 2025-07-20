from pydantic import BaseModel
class DialInDto(BaseModel):
    beansName: str = None
    roastDate: str = None
    dialedBy: str = None
    dose: float = None
    time: float = None
    calibrationYield: float = None
    sweetSpot: float = None
    grinder: str = None
    grindSize: float = None
    mouthFeel: str = None
    black: str = None
    blackNotes: str = None
    white: str = None
    whiteNotes: str = None