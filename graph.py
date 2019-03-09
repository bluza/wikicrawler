from collections import defaultdict

class Graph(object):

    def __init__(self, connection):
        self.graph = defaultdict(set)
        self.connection = connection
        self.add_connection(connection)

    def add_connection(self, connection):
        for node1, node2 in connection:
            self.add(node1,node2)

    def add(self,node1, node2):
        self.graph[node1].add(node2)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.graph))

#connections = [('A', 'B'), ('B', 'C'), ('B', 'D'),
#                 ('C', 'D'), ('E', 'F'), ('F', 'C')]

#g = Graph(connections)

#t= print()
