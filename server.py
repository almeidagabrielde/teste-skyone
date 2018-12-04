import uuid
from User import User
from Server import Server

class server:
    def __init__(self, uMax):
        self.id = str (uuid.uuid5())
        self.uMax = uMax
        self.userList = []

    def __add__(self, User):
        if len(self.userList) <= self.uMax:
            self.userList.append(User)
            return self
        else:
            return False

    def getUser(self):
        return len(self.userList)

    def removeUser(self, User):
        self.userList.remove(User)

    def runT(self):
        self.runnerdT += 1
        self.runTikUser()

class ServerList:
    def __init__(self, tTask, uMax):
        self.Server = []
        self.tTask = tTask
        self.uMax = uMax
        self.totalRun = 0

    def getServer(self):
        user = ""
        for sever in self.Server:
            user = str(server.getUser())
        if server.getUser() ==0:
            self.Server.remove(server)

    def runTiks(self):
        for server in self.Server:
            server.runT()
            self.totalRun = server.runT()
            if server.getUser() = 0:
                self.Server.remove(server)

    def addServer(self, user):
        self.Server.append(server(self.uMax).addUser(user))

    def addUser(self, user):
        add = False
        if len(self.Server) > 0
            if len (server.userList) < self.uMax:
                break

            if add:
                return 0
            elif self.addServer(user)

        else:
                print("Número máximo de usuários atingido, por favor aguarde")