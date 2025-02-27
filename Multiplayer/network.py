import socket
import pickle
from IPsafe import IPSafe

class Network : # Client <-> server connect chain
    def __init__(self, IPtool) :
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Server -> connect
        self.server = IPSafe().GetIP(IPtool)
        self.port = 28578
        self.addr = (self.server, self.port)
        self.p = self.connect()
        print(self.client)

    def getP(self) :
        return self.p

    def connect(self) :
        try :
            self.client.connect(self.addr) # connect
            return pickle.loads(self.client.recv(2048))
        except :
            pass

    def recv(self, data):
        try:
            self.client.send(pickle.dumps(data))
            data = self.client.recv(2048)
            if not data:  # 서버가 응답하지 않을 경우
                print("No data received. Connection may be closed.")
                return None
            return pickle.loads(data)
        except socket.error as e:
            print(f"Socket error: {e}")
            return None

    # def send(self, data) :
    #     try :
    #         self.client.send(pickle.dumps(data))
    #         return pickle.loads(self.client.recv(2048))
    #     except socket.error as e :
    #         print(e)