import time

#Bah Humbug

print("Lets Do some Dijkstra")

class Node:

    def __init__(self, name):
        self.name = name
        self.weight = 100
        self.start = False
        self.end = False
        self.closed = False
        self.bridges = []
        self.bridgesWeight = []
        print ("Node %d created"  % (self.name,))
    
    def addBridge(self, name, weight):
        self.bridges.append(name)
        self.bridgesWeight.append(weight)
        print ("Bridge created between %d and %d of weight %d " % ( self.name, name, weight, ))
        
    def listBridges(self):
        print ("The bridges for %d are:" % ( self.name, ))
        bridges = [[] for i in range(len(self.bridges))]
        for index in range(len(self.bridges)):
            bridges[index].append(self.bridges[index])
            bridges[index].append(self.bridgesWeight[index])
        return bridges

def wait():
    time.sleep(5)

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
    node[1].addBridge(2, 2)
    node[1].addBridge(5, 3)
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
    print(node[0].listBridges())
    print(node[1].listBridges())
    print(node[2].listBridges())
    print(node[3].listBridges())
    print(node[4].listBridges())
    print(node[5].listBridges())
    print(node[6].listBridges())
    
    node[0].start = True
    node[0].weight = 0
    node[5].end = True

    working = True
    lastNode = 10
    while (working):
        currentNode = 4
        for i in range(7):
            if (node[i].weight < node[currentNode].weight) and (node[i].closed == False):
                currentNode = i;
        currentBridges = node[currentNode].listBridges();
        
        if currentNode == lastNode:
            print("The end has been found")
            break
        else:
            print("No end found yet")
        

        for index in range(len(currentBridges)):
            if (node[currentBridges[index][0]].weight > node[currentNode].weight + currentBridges[index][1]):
                node[currentBridges[index][0]].weight = node[currentNode].weight + currentBridges[index][1]
            print(node[currentBridges[index][0]].weight)
                
        
        node[currentNode].closed = True
        
        lastNode = currentNode;
        wait()

    print(node[0].weight)
    print(node[1].weight)
    print(node[2].weight)
    print(node[3].weight)
    print(node[4].weight)
    print(node[5].weight)
    print(node[6].weight)

start()
