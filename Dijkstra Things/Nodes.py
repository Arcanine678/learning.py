#Bah Humbug

print("Lets Dick some Dijkstra")

class Node:

    def __init__(self, name):
        self.name = name
        self.bridges = []
        self.bridgesWeight = []
        print ("Node " + self.name + " created")
    
    def addBridge(self, name, weight):
        self.bridges.append(name)
        self.bridgesWeight.append(weight)
        print ("Bridge created between " + self.name + " and " + name + " of weight %d " % (weight,))
        
    def listBridges(self):
        print ("The bridges for " + self.name + " are:")
        for index in range(len(self.bridges)):
            print (self.bridges[index])
            print (self.bridgesWeight[index])
        

def start():

    node1 = Node("A")
    node2 = Node("B")

    node1.addBridge("B", 5)
    node2.addBridge("A", 10)

    node1.listBridges()
    node2.listBridges()



start()
