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
        print(self.p)

    def getP(self) :
        return self.p

    def connect(self) :
        try :
            self.client.connect(self.addr) # connect
            return pickle.loads(self.client.recv(2048))
        except :
            pass

    def recv(self) :
        try :
            self.client.send(pickle.dumps(-1))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e :
            print(e)

    def send(self, data) :
        try :
            self.client.send(pickle.dumps(data))
        except socket.error as e :
            print(e)