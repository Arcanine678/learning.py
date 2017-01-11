import time


print("Lets Do some Dijkstra")

#the node class references each point on the map
class Node:

    #this is the initialisation of the node class
    def __init__(self, name):
        self.name = name
        self.weight = 100
        self.start = False
        self.end = False
        self.closed = False
        self.path = 0
        self.bridges = []
        self.bridgesWeight = []
        print ("Node %d created"  % (self.name,))
    
    #this method adds a bridge between two nodes
    #It only adds a one way bridge, so a matching node must be added for a 2 way movement map
    def addBridge(self, name, weight):
        self.bridges.append(name)
        self.bridgesWeight.append(weight)
        print ("Bridge created between %d and %d of weight %d " % ( self.name, name, weight, ))
    
    #this method returns a list of lists of each bridge connected to the chosen node       
    def listBridges(self):
        print ("Analyzing bridges from node %d:" % ( self.name, ))
        bridges = [[] for i in range(len(self.bridges))]
        for index in range(len(self.bridges)):
            bridges[index].append(self.bridges[index])
            bridges[index].append(self.bridgesWeight[index])
        return bridges

#this method is not neccacary but makes the program look nicer
def wait():
    time.sleep(1)

#this method is where everything happens
def start():

    #this method is inside start so that it has access to the created nodes
    def findPath(i):
        print(node[i].path)
        if(node[i].path == 0):
            print("The path is finished")
        else:
            findPath(node[i].path)

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
                node[currentBridges[index][0]].path = currentNode
            print(node[currentBridges[index][0]].weight)
                     
        node[currentNode].closed = True
        
        lastNode = currentNode;
        wait()

    print("The shortest path from node %d to %d is:" % ( node[0].name, node[5].name,))
    
    findPath(5)
    
start()
