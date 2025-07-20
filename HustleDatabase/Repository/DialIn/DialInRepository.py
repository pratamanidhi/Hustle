from HustleDatabase.ConnectionLog import ConnectionLogs as Connection
import uuid

db = Connection()
class DialInRepository():
    def __init__(self) -> None:
        pass

    def GetDialInAllData(self):
        query = "select * from DialIn"
        result = db.Execute(query)
        return result

    def InsertDialInData(self, model):
        guid = str(uuid.uuid4())
        query = f'insert into DialIn(guid, beansName, date, roastDate, dialedBy, dose, time, calibrationYield, sweetSpot, grinder, grindSize, mouthFeel, black, blackNotes, white, whiteNotes, updatedAt) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        result = db.Execute(query, (
            guid,
            model.beansName,
            model.date,
            model.roastDate,
            model.dialedBy,
            model.dose,
            model.time,
            model.calibrationYield,
            model.sweetSpot,
            model.grinder,
            model.grindSize,
            model.mouthFeel,
            model.black,
            model.blackNotes,
            model.white,
            model.whiteNotes,
            model.updatedAt
        ))
        return result