from HustleDatabase.ConnectionLog import ConnectionLogs as Connection
import uuid
import json

db = Connection()
class DialInRepository():
    def __init__(self) -> None:
        pass

    def GetDialInAllData(self):
        query = "SELECT * FROM DialIn order by date desc"
        rows = db.Execute(query)
        result = []

        for row in rows:
            rowDict = dict(row)
            try:
                if rowDict["dialedBy"]:
                    rowDict["dialedBy"] = json.loads(rowDict["dialedBy"])
            except json.JSONDecodeError:
                rowDict["dialedBy"] = []

            try:
                if rowDict["tools"]:
                    rowDict["tools"] = json.loads(rowDict["tools"])
            except json.JSONDecodeError:
                rowDict["tools"] = []

            result.append(rowDict)

        return result

    def InsertDialInData(self, model):
        guid = str(uuid.uuid4())
        dialedBy = json.dumps(model.dialedBy) if model.dialedBy else None
        tools = json.dumps(model.tools) if model.tools else None
        query = f'insert into DialIn(guid, beansName, date, roastDate, dialedBy, dose, time, calibrationYield, sweetSpot, tools, grindSize, mouthFeel, black, espressoNotes, americanoNotes, white, cappuccinoNotes, latteNotes, updatedAt) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        result = db.Execute(query, (
            guid,
            model.beansName,
            model.date,
            model.roastDate,
            dialedBy,
            model.dose,
            model.time,
            model.calibrationYield,
            model.sweetSpot,
            tools,
            model.grindSize,
            model.mouthFeel,
            model.black,
            model.espressoNotes,
            model.americanoNotes,
            model.white,
            model.cappuccinoNotes,
            model.latteNotes,
            model.updatedAt
        ))
        return result

    def DeleteDialIn(self, id):
        query = f"delete from DialIn where guid = ?"
        result = db.Execute(query, (id,))
        return result