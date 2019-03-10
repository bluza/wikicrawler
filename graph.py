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

    def write(self, path):
        with open(path, 'w') as file:
            for key, value in self.graph.items():
                print ("Key: "+key+": \n")
                file.write("Key: "+key+": ")
                for val in value:
                    print("\t"+val)
                    file.write("\t"+val)
                file.write(" \n")
        print("File written.")

    def readfromfile(self, path):
        with open(path, 'r') as file:
            pass



    def __str__(self):
        return '{}({} \n)'.format(self.__class__.__name__, dict(self.graph))

#connections = [('A', 'B'), ('B', 'C'), ('B', 'D'),
#                 ('C', 'D'), ('E', 'F'), ('F', 'C')]

#g = Graph(connections)

#t= print()
