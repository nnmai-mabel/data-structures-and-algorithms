class GraphList:
    def __init__(self, directed) -> None:
        self.directed = directed
        self.edges = 0
        self.vertices = []
        self.graph = {}

    def add_edge(self, source, destination):
        # print(len(self.graph))
        if source < 0 or destination < 0:
            print("index out of bound")
        
        if source not in self.graph:
            self.graph[source] = []

        if destination not in self.graph[source]:
            self.graph[source].append(destination)

            self.edges += 1 # if there is an edge in undirected, minus edges

        if not self.directed:
            if destination not in self.graph:
                self.graph[destination] = []
            if source not in self.graph[destination]:
                self.graph[destination].append(source)
        
        if source not in self.vertices:
            self.vertices.append(source)

        if destination not in self.vertices:
            self.vertices.append(destination)

    # In undirected, if delete edge from source -> destination, also delete edge from destination -> source
    def remove_edge(self, source, destination):
        if source < 0 or destination < 0:
            print("index out of bound")
        
        if source not in self.graph:
            print("No edge with source provided")

        if destination in self.graph[source]:
            self.graph[source].remove(destination)
            
            self.edges -= 1

            # Remove vertices
            # Check if the item is not a key in the dictionary
            # Check if the item is not present in the value list of any key in the dictionary
            if destination not in self.graph and not any(destination in sublist for sublist in self.graph.values()):
                self.vertices.remove(destination)

        if not self.directed:
            if destination not in self.graph:
                print("no edge with destination provided")
            if source in self.graph[destination]:
                self.graph[destination].remove(source)
                    
    def has_edge(self, source, destination):
        if source not in self.graph:
            return False
        
        if len(self.graph[source]) == 0:
            return False
        
        return destination in self.graph[source]

    def print_graph_list(self):
        print("Vertices: ", self.vertices)
        print("Edges: ", self.edges)

        print("Graph")
        print(self.graph)

directed_graph_list = GraphList(True)
directed_graph_list.add_edge(1, 4)
directed_graph_list.add_edge(2, 4)
directed_graph_list.add_edge(3, 4)
directed_graph_list.add_edge(5, 4)
# print(directed_graph_list.has_edge(1, 4))
# print(directed_graph_list.has_edge(4, 1))
directed_graph_list.print_graph_list()
directed_graph_list.remove_edge(1, 4)
directed_graph_list.remove_edge(2, 4)
directed_graph_list.remove_edge(3, 4)
directed_graph_list.remove_edge(5, 4)
print("after delete edge")
directed_graph_list.print_graph_list()
print("Add again")
directed_graph_list.add_edge(1, 4)
directed_graph_list.add_edge(2, 4)
directed_graph_list.add_edge(3, 4)
directed_graph_list.add_edge(5, 4)
directed_graph_list.print_graph_list()

print("\nUNDIRECTED")
undirected_graph_list = GraphList(False)
undirected_graph_list.add_edge(1, 4)
undirected_graph_list.add_edge(2, 4)
undirected_graph_list.add_edge(3, 4)
undirected_graph_list.add_edge(5, 4)
# print(undirected_graph_list.has_edge(1, 4))
# print(undirected_graph_list.has_edge(4, 1))
undirected_graph_list.print_graph_list()

undirected_graph_list.remove_edge(1, 4)
undirected_graph_list.remove_edge(2, 4)
undirected_graph_list.remove_edge(3, 4)
undirected_graph_list.remove_edge(5, 4)
print("\nafter delete edge")
undirected_graph_list.print_graph_list()

print("\nAdd again")
# undirected_graph_list.add_edge(1, 4)
undirected_graph_list.add_edge(2, 4)
undirected_graph_list.add_edge(3, 4)
undirected_graph_list.add_edge(5, 4)
undirected_graph_list.print_graph_list()

print("\nremove again")
undirected_graph_list.remove_edge(4, 2)
undirected_graph_list.print_graph_list()