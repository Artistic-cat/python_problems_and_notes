
def createGraph(projects, dependencies):
    projectGraph={}
    for project in projects:
        projectGraph[project]=[]
    for pairs in dependencies:
        projectGraph[pairs[0]].extend(pairs[1])
    return projectGraph

def withDependencies(graph):
    dep=set()
    for project in graph:
        dep=dep.union(set(graph[project]))
    return dep

def wodependencies(graph):
    wdep=set()
    for project in graph:
        pass