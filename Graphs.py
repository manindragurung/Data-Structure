
class Graph:
    def __init__(self):
        self.adj_list = {}

    def addVertex(self,vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def addEdge(self,v1,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)    
            return True
        return False
        

    def removeEdge(self,v1,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except: ValueError
            return True
        return False

    def removeVertex(self,vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True


    def printGraph(self):
        for vertex in self.adj_list:
            print(vertex , ': ' ,self.adj_list[vertex])

graph = Graph()
graph.addVertex(1)
graph.addVertex(2)
graph.addVertex(3)
graph.addVertex(4)
graph.addEdge(1,3)
graph.addEdge(1,2)
graph.addEdge(4,2)
graph.removeEdge(1,4)
graph.removeVertex(1)
graph.printGraph()