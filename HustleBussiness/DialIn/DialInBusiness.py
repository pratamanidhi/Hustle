from HustleDatabase.Repository.DialIn.DialInRepository import DialInRepository as Repository
from HustleDatabase.Model.DialIn.DialInModel import DialInModel as Model
from datetime import datetime, date

repo = Repository()
model = Model()
class DialInBusiness():
    def __init__(self) -> None:
        pass

    def GetAllDialIn(self):
        result = repo.GetDialInAllData()
        return result

    def InputDialIn(self, input):
        model.beansName = input.beansName
        model.date = date.today().isoformat()
        model.roastDate = input.roastDate
        model.dialedBy = input.dialedBy
        model.dose = input.dose
        model.time = input.time
        model.calibrationYield = input.calibrationYield
        model.sweetSpot = input.sweetSpot
        model.tools = input.tools
        model.grindSize = input.grindSize
        model.mouthFeel = input.mouthFeel
        model.black = input.black
        model.blackNotes = input.blackNotes
        model.white = input.white
        model.whiteNotes = input.whiteNotes
        model.updatedAt = str(datetime.now())

        result = repo.InsertDialInData(model)
        return result

