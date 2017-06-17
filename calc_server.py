__author__ = "Shlomy Balulu"
"""
Simple twisted server
"""


from twisted.internet import reactor, protocol
from twisted.python import log
import sys
from calculator import Calculator


log.startLogging(sys.stdout)

class Echo(protocol.Protocol):
    def __init__(self):
        print protocol.Protocol
        self.calculator_instance = Calculator()

    def dataReceived(self, data):
        response = self.calculator_instance.calculate(data)
        self.transport.write(response)


def main():
    factory = protocol.ServerFactory()
    factory.protocol = Echo
    reactor.listenTCP(8000, factory)
    reactor.run()


# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()
