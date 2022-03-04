from ip import Ip

class Router:
    
    def __init__(self, L):
        self.num += 1
        self.L = L
        self.name = "Rt" + num
    
    def addInterface(self, ip):
        R1.addInterfarce([Ip("195.134.50.13/24")])
        self.name.append([Ip(ip)])
        
    def getIpByInterface(self, name):
        pass
    
    def removeInterface(self, ip):
        R1.removeInterfarce("132.154.40.1")
    
R1 = Routeur([Ip("10.53.1.2/8"), Ip("132.154.40.1/16")])