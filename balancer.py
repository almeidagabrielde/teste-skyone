import  sys
from ServerList import ServerList
from Server import Server
from User import User


try:
 arquivo = sys.argv[1]

 tTask = 5
 uMax = 10

 systemList = ServerList(5,10)
 f = open(arquivo,"r")
 fOut = open("output-file.txt","w")

 for line in f :systemList.runAllTiks()
 if len(line) > 1:
if int(float(line)) >= 0 :
 for x in range(int(float(line))) :
  systemList.addUser(User(tTask))
  fOut.write(systemList.getServers() + "\n")
  fOut.write("$ : " + str(systemList.totalRunned))
except:
print("Não foi possível acessar o servidor")