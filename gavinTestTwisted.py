#coding=UTF-8

#case1 hello twisted
#def hello():
#    print "I am gavin cui"
#
#from twisted.internet import reactor
#reactor.callWhenRunning(hello)
#
#print "Start reactor"
#reactor.run()


#case2 stack
#import traceback
#
#def stack():
#    print "python stack"
#    traceback.print_stack()
#    
#from twisted.internet import reactor
#
#reactor.callWhenRunning(stack)
#reactor.run()
    
#case3 countdown
#import time
#from twisted.internet import reactor
#   
#class Countdown(object):
#    
#    counter = 5
#    
#    def count(self):
#        if self.counter == 0:
#            reactor.stop()
#        else:
#            print self.counter,"....."
#            self.counter -= 1
#            reactor.callLater(1,self.count)
#
#reactor.callWhenRunning(Countdown().count)
#
#print "start!!!"
#reactor.run()
#print "Stop!!!"



#def fallDown():
#    raise Exception("i am fall down")
#
#def upAgain():
#    print "but i get up again"
#    reactor.stop()
#
#from twisted.internet import reactor
#    
#reactor.callWhenRunning(fallDown)
#reactor.callWhenRunning(upAgain)
#
#print "Startting the reactor"
#reactor.run()

    
#twisted  事件循环测试    
#from twisted.internet import reactor
#import time
#
#def printTime():
#    print 'Current time is',time.strftime("%H:%M:%S")
#def stopReactor():
#    print "Stopping reactor"
#    reactor.stop()
#reactor.callLater(1,printTime)
#reactor.callLater(2,printTime)
#reactor.callLater(3,printTime)
#reactor.callLater(4,printTime)
#reactor.callLater(5,stopReactor)
#print 'Running the reactor ...'
#reactor.run()
#print 'Reactor stopped.'

#twisted 建立TCP连接
#from twisted.internet import reactor, protocol
#
#class QuickDisconnectedProtocol(protocol.Protocol):
#    def connectionMade(self):
#        print "Connection to %s."%self.transport.getPeer().host
#        self.transport.loseConnection()
#
#class BasicClientFactory(protocol.ClientFactory):
#    
#    protocol = QuickDisconnectedProtocol
#    
#    def clientConnectionLost(self,connector,reason):
#        print "Lost connection %s "%reason.getErrorMessage()
#        reactor.stop()
#        
#    def clientConnectionFailed(self,connector,reason):
#        print "Connection failed %s"%reason.getErrorMessage()
#        reactor.stop()
#        
#reactor.connectTCP('www.google.com',80,BasicClientFactory())
#reactor.run()



#twisted deferred case
from twisted.internet import reactor, defer, protocol

class CallbackAndDisconectProtocol(protocol.Protocol):

    def connectionMade(self):
        self.factory.deferred.callback("Connected!!!")
        self.transport.loasConnection()

class ConnectionTestFactory(protocol.ClientFactory):
    
    protocol = CallbackAndDisconectProtocol
    
    def __init__(self):
        self.deferred = defer.Deferred()
    
    def clientConnectionFailed(self, connector, reason):
        self.deferred.callback(reason)

def testConnect(host, port):
    testFactory  = ConnectionTestFactory()
    reactor.connectTCP(host,port,testFactory)
    return testFacoory.deferred

def handleSucces(result, port):
    print "Connect to port %i"%port
    reactor.stop()
    
def handleFailure(failure, port):
    print "Error connecting to port %i: %s"%(port, failure.getErrorMessage())
    reactor.stop()

if __name__ == "__main__":
    import sys
    if not len(sys.argv) == 3:
        print "Usage: connectiontest.py host port"
        sys.exit(1)
        host = sys.argv[1]
        port = int(sys.argv[2])
        
        connecting = testConnect(host, port)
        connecting.addCallback(handleSuccess, port)
        connecting.addErrback(handleFailure, port)
        reactor.run(1)
        


        
        
        
        
        