__author__ = "Shlomy Balulu"
"""
Simple twisted client
"""


from twisted.internet import reactor, protocol
import json
from args_parser import ArgsParser

args_parser = ArgsParser()

class EchoClient(protocol.Protocol):

    def connectionMade(self):
        self.transport.write(json.dumps(args_parser.get_args()))

    def dataReceived(self, data):
        print data
        self.transport.loseConnection()

    def connectionLost(self, reason):
        pass


class EchoFactory(protocol.ClientFactory):
    protocol = EchoClient

    def clientConnectionFailed(self, connector, reason):
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        reactor.stop()


def main():
    f = EchoFactory()
    reactor.connectTCP("localhost", 8000, f)
    reactor.run()

if __name__ == '__main__':
    main()
