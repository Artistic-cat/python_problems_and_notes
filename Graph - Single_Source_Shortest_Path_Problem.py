"""
Cheapest price from root to all other nodes.

BFS
Dijkstra
Bellman Ford
"""


class Graph:
    def __init__(self,gdict={}):
        self.gdict=gdict
    
    def bfs(self,start,end):
        queue=[]
        queue.append([start])
        while queue:
            path=queue.pop(0)
            node=path[-1]
            if node==end:
                return path
            for adj in self.gdict.get(node,[]):
                newPath=list(path)
                newPath.append(adj)
                queue.append(newPath)

