from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class Echo(DatagramProtocol):

    def datagramReceived(self, data, (host, port)):
        data = str(data).upper()
        print(data)
        self.transport.write(data, (host, port))

reactor.listenUDP(1234, Echo())
reactor.run()
