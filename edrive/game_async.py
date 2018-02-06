from twisted.internet import protocol, reactor, endpoints
from time import sleep
from random import randint

class MyProtoclol(protocol.Protocol):
    def dataReceived(self, data):
        sleep(randint(1, 5))
        self.transport.write(data)

class MyFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return MyProtoclol()


endpoints.serverFromString(reactor, "tcp:8080").listen(MyFactory())
reactor.run()
