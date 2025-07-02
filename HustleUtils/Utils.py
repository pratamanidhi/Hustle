from datetime import datetime

class Utils():
    def __init__(self) -> None:
        pass

    def FormatedDate(self, data):
        if isinstance(data, datetime):
            return data.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return data