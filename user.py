import uuid

class User:
    def __init__(self, tTask):
        self.id = str (uuid.uuid5())
        self.tTask = tTask
        self.runnedTUser(self) = 0;

    def runnedTUser(self):
        self.Tuser += 1
        return int(self.runnedTUser)