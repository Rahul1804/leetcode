class AdjNode:
    """
    A class to represent the adjacency list of the node
    """

    def __init__(self, data):
        self.vertex = data
        self.next = None


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    def add_edge(self, source, destination):
        node = AdjNode(destination)
        node.next = self.graph[source]

    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


def dfs(graph, source):

    visited = [False] * (len(graph.graph))

    stack = []

    result = ""

    stack.append(source)

    while stack:
        if not visited[source]:
            result += str(source)
            visited[source] = True

        while graph.graph[source] is not None:
            data = graph.graph[source].vertex
            if not visited[data]:
                stack.append(data)
            graph.graph[source] = graph.graph[source].next
