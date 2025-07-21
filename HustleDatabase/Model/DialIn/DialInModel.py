from pydantic import BaseModel
class DialInModel(BaseModel):
    guid: str = None
    beansName: str = None
    date: str = None
    roastDate : str = None
    dialedBy: str = None
    dose: float = None
    time: float = None
    calibrationYield: float = None
    sweetSpot: float = None
    tools: str = None
    grindSize: float = None
    mouthFeel: str = None
    black: str = None
    blackNotes: str = None
    white: str = None
    whiteNotes: str = None
    updatedAt: str = None

