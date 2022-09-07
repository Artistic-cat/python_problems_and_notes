"""
Graphs
"""

# class Graph:
#     def __init__(self,gdict={}):
#         self.gdict={}

class AdjacentGraph:
    def __init__(self):
        self.gdict={}

    def addVertex(self,vertex):
        self.gdict[vertex]=[]
    
    def removeVertex(self,vertex):
        if vertex in self.gdict.keys():
            for i in self.gdict[vertex]:
                self.gdict[i].remove(vertex)
            del self.gdict[vertex]
            

    def addEdge(self,vertex1,vertex2):
        if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys():
            self.gdict[vertex1].append(vertex2)
            self.gdict[vertex2].append(vertex1)
    
    def printGraph(self):
        for vertex in self.gdict:
            print(vertex,":",self.gdict[vertex])

    def removeEdge(self,vertex1,vertex2):
        if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys():
            self.gdict[vertex1].remove(vertex2)
            self.gdict[vertex2].remove(vertex1)

    def BFT(self,start):
        visited={}
        queue=[start]
        while queue!=[]:
            current=queue.pop(0)
            if current not in visited.keys():
                visited[current]=1
                print(current)
                for i in self.gdict[current]:
                    if i not in visited.keys():
                        queue.append(i)

    def DFT(self,start):
        visited=[]
        stack=[start]
        while stack!=[]:
            current=stack.pop()
            if current not in visited:
                visited.append(current)
                print(current)
                for i in self.gdict[current]:
                    if i not in visited:
                        stack.append(i)

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph=defaultdict(list)
        self.vertices=vertices
    
    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def topologicalSortUtil(self,v,visited,stack):
        visited.append(v)
        for i in self.graph[v]:
            if i not in visited:
                self.topologicalSortUtil(i, visited, stack)
        stack.insert(0,v)

    def topologicalSort(self):
        visited=[]
        stack=[]
        for k in list(self.graph):
            if k not in visited:
                self.topologicalSortUtil(k,visited,stack)
        print(stack)


customGraph=Graph(8)
# customGraph.addVertex("A")
# customGraph.addVertex("B")
# customGraph.addVertex("C")
# customGraph.addVertex("D")
# customGraph.addVertex("E")
# customGraph.addVertex("F")
# customGraph.addVertex("G")
# customGraph.addVertex("H")
# customGraph.printGraph()
customGraph.addEdge("A","C")
customGraph.addEdge("B","C")
customGraph.addEdge("B","D")
customGraph.addEdge("C","E")
customGraph.addEdge("E","H")
customGraph.addEdge("E","F")
customGraph.addEdge("F","G")
customGraph.addEdge("D","F")
# customGraph.printGraph()
customGraph.topologicalSort()
