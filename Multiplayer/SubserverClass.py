class PlayerInfo :
    def __init__(self, PN) :
        self.playerInfo = {}
        self.playerInfo['CurrentKey'] = []
        self.playerInfo['Nickname'] = f"P{PN+1}"
        self.playerInfo['message'] = (1, "")
        self.playerInfo['SR'] = {'card':[], 'cardsImg':""}

    def update(self, content) :
        RightSave = ['CurrentKey']
        ServerRecvList = ['card', 'cardsImg']

        for k, v in content.items() :
            try :
                if k in RightSave :
                    self.playerInfo[k] = v
                if k in ServerRecvList :
                    self.playerInfo['SR'][k] = v
            except Exception as e :
                print(e)

    def RecvInfo(self, key) :
        try :
            return self.playerInfo[key]
        except Exception as e:
            print(e)

    def RecvData(self) :
        recvdata = {}
        recvDataList = ['Nickname', 'message']

        for item in recvDataList :
            recvdata[item] = self.RecvInfo(item)

        return recvdata
    
    def RecvPlayer(self) :
        return self.playerInfo