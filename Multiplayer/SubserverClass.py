class PlayerInfo :
    def __init__(self, PN) :
        self.playerInfo = {}
        self.playerInfo['CurrentKey'] = []
        self.playerInfo['Nickname'] = f"P{PN+1}"
        self.playerInfo['message'] = (f"P{PN+1}", 0, "") # Nick/time/prompt

    def update(self, content) :
        RightSave = ['CurrentKey', 'message']

        for k, v in content.items() :
            if k in RightSave :
                self[k] = v

    def RecvInfo(self, key) :
        try :
            return self.playerInfo[key]
        except :
            print("error happend")

    def RecvData(self) :
        recvdata = {}
        recvDataList = ['message']

        for item in recvDataList :
            recvdata[item] = self.RecvInfo(item)

        return recvdata