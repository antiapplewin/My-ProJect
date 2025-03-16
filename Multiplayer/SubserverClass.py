class PlayerInfo :
    def __init__(self, PN) :
        self.playerInfo = {}
        self.playerInfo['CurrentKey'] = []
        self.playerInfo['Nickname'] = f"P{PN+1}"
        self.playerInfo['message'] = (1, "")
        self.playerInfo['action'] = ()
        self.playerInfo['SR'] = {'card':[], 'showingCard':[], 'handChip':0}

    def update(self, content) :
        ServerRecvList = ['card', 'showingCard']

        for k, v in content.items() :
            try :                    
                if k in ServerRecvList :
                    self.playerInfo['SR'][k] = v
                else :
                    self.playerInfo[k] = v
            except Exception as e :
                print(e)

    def RecvInfo(self, key) :
        try :
            SRs = ['card', 'showingCard', 'handChip']
            if (key in SRs) :
                return self.playerInfo['SR'][key]
            return self.playerInfo[key]
        except Exception as e:
            print(e)

    def RecvData(self) :
        recvdata = {}
        recvDataList = ['Nickname', 'message', 'showingCard', 'handChip']

        for item in recvDataList :
            recvdata[item] = self.RecvInfo(item)

        return recvdata
    
    def RecvPlayer(self) :
        return self.playerInfo