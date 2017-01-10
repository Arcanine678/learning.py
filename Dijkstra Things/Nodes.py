import time

#Bah Humbug

print("Lets Do some Dijkstra")

class Node:

    def __init__(self, name):
        self.name = name
        self.weight = 100
        self.start = False
        self.end = False
        self.bridges = []
        self.bridgesWeight = []
        print ("Node %d created"  % (self.name,))
    
    def addBridge(self, name, weight):
        self.bridges.append(name)
        self.bridgesWeight.append(weight)
        print ("Bridge created between %d and %d of weight %d " % ( self.name, name, weight, ))
        
    def listBridges(self):
        print ("The bridges for %d are:" % ( self.name, ))
        if (len(self.bridges) == 0):
            print("there are no bridges for " + self.name)
        else:
            for index in range(len(self.bridges)):
                print (self.bridges[index])
                print (self.bridgesWeight[index])


def Wait():
    time.sleep(0.5)

def start():

    node = []

    #Add all the nodes
    node.append(Node(0))
    node.append(Node(1))
    node.append(Node(2))
    node.append(Node(3))
    node.append(Node(4))
    node.append(Node(5))
    node.append(Node(6))

    print()
    print()

    #Add all the bridges
    node[0].addBridge(2, 1)
    node[0].addBridge(3, 2)
    print()
    node[1].addBridge(2, 3)
    node[1].addBridge(5, 2)
    print()
    node[2].addBridge(0, 1)
    node[2].addBridge(1, 2)
    node[2].addBridge(3, 1)
    node[2].addBridge(4, 3)
    print()
    node[3].addBridge(0, 2)
    node[3].addBridge(2, 1)
    node[3].addBridge(6, 1)
    print()
    node[4].addBridge(2, 3)
    node[4].addBridge(5, 2)
    print()
    node[5].addBridge(1, 3)
    node[5].addBridge(4, 2)
    node[5].addBridge(6, 1)
    print()
    node[6].addBridge(3, 1)
    node[6].addBridge(5, 1)
    print()
    print()
    node[0].listBridges()
    node[1].listBridges()
    node[2].listBridges()
    node[3].listBridges()
    node[4].listBridges()
    node[5].listBridges()
    node[6].listBridges()
    
    node[0].start = True
    node[0].weight = 0
    node[5].end = True

    while (node[5].weight == 100):
        print("No end found yet")
        
        Wait()

start()