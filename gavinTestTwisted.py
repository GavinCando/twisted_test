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




        
        
        
        
        