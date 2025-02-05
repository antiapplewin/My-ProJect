class IPSafe :
    def __init__(self) :
        self.IPlist = {"101" : "192.168.0.50","102" : "192.168.137.243", "103" : '192.168.153.243'}

    def GetIP(self, shortIP) :
        return self.IPlist[shortIP]