#Graph

class Graph:
    def __init__(self):
        self.adjDict = {}

    def addVertex(self, vertex):
        if vertex not in self.adjDict.keys():
            self.adjDict[vertex] = []
            return True
        else:
            return False
        
    def addEdge(self, vertex1, vertex2):
        if vertex1 in self.adjDict.keys() and vertex2 in self.adjDict.keys():
            self.adjDict[vertex1].append(vertex2)
            self.adjDict[vertex2].append(vertex1)
            return True
        else:
            return False
        
    def removeEdge(self, vertex1, vertex2):
        if vertex1 in self.adjDict.keys() and vertex2 in self.adjDict.keys():
            try:
                self.adjDict[vertex1].remove(vertex2)
                self.adjDict[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        else:
            return False
        
    def removeVertex(self, vertex):
        if vertex in self.adjDict.keys():
            for v in self.adjDict[vertex]:  # remove all edges to vertex
                self.adjDict[v].remove(vertex)
            self.adjDict.pop(vertex)
            return True
        else:
            return False
        
    def printGraph(self):
        for vertex in self.adjDict.keys():
            print(vertex, ":", self.adjDict[vertex])

# Test
g = Graph()
g.addVertex("A") # True
g.addVertex("B") # True
g.addVertex("C") # True
g.addVertex("D") # True
g.addEdge("A", "B") # True
g.addEdge("A", "C") # True
g.addEdge("B", "D") # True
g.addEdge("C", "D") # True
g.printGraph()  # A : ['B', 'C'] B : ['A', 'D'] C : ['A', 'D'] D : ['B', 'C']
g.removeEdge("A", "B") # True
g.printGraph()  # A : ['C'] B : ['D'] C : ['A', 'D'] D : ['B', 'C']
g.removeVertex("C") # True
g.printGraph()  # A : [] B : ['D'] D : ['B']
g.removeVertex("E")  # False
g.removeEdge("A", "B")  # True
g.removeEdge("A", "E")  # False
g.addEdge("A", "B")  # True
g.addEdge("A", "E")  # False
g.addVertex("A")  # False
g.addVertex("E")  # True
g.printGraph()  # A : ['B'] B : ['A', 'D'] D : ['B'] E : []

