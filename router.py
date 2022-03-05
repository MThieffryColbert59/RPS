from ip import Ip

class Router:
    
    Num = 0
    def __init__(self, L):
        Routeur.Num += 1
        self.interfaces = list(L)
        self.name = f"Rt{Routeur.Num}"
        self.neighborns = {}
        for n in range(len(self.interface)):
            self.neighborns['int'+str(n)] = {'state':False, 'name':None, 'cost'0}
    
    def addInterface(self, ip):
        self.interface.append(ip)
        self.neighborns['int'+str(len(self.interface)-1)] = {'state':False, 'name':None, 'cost'0}
        
       
    def getIpByInterface(self, name):
        return self.interface[int(name.split('int-')[-1])]
    
    def removeInterface(self, ip):
        self.interface.remove(ip)
        self.neighborns.pop()