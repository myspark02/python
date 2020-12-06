class Graph :
    # init arguments  is an arrary of tuples representing edges between nodes.
    # from the edges, build a dictionary where a key is a starting city 
    # and corresponding value is an array of cities directly reachable from the starting city.

    def __init__(self, edges) :
        self.graph_dict = {}
        for start, end in edges :
            if start in self.graph_dict :
                self.graph_dict[start].append(end)
            else :
                self.graph_dict[start] = [end]

    def get_paths(self, start, end, path=[]) :
        # recursive function
        # append start city to the path list which represents a path from a city to the start city.
        print('start:', start, ' end:', end)
        path = path + [start]
        # path.append(start)

        # if start city and end city is the same then no more calculation is needed.
        if start == end :
            return [path]

        # if start city is not in the grapth dictionary, which means there is no directly reachable city 
        # from that city, then return empty array.
        if start not in self.graph_dict :
            return []
        # print('path:', path)
        paths = [] # all paths to end city 
        # for every city directly reachable from start city
        #   append a path from that city to end city to the paths list
        for node in self.graph_dict[start]:
            # print(node)
            if node not in path : # prevent a cycle 
                paths_to_end = self.get_paths(node, end, path) 
                # print('path_to_end:', path_to_end)
                for a_path in paths_to_end :
                    paths.append(a_path)

        return paths

    def get_shortest_path(self, start, end, path=[]) :

        path = path + [start]

        if start == end :
            return path

        if start not in self.graph_dict : # start is not a city in any routes
            return None
        
        shortest_path = None

        for node in self.graph_dict[start] :
            if node not in path :
                a_path = self.get_shortest_path(node, end, path) 
                if shortest_path is None or len(a_path) < len(shortest_path) :
                        shortest_path = a_path

        return shortest_path

if __name__ == '__main__' :
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    route_graph = Graph(routes)

    start = "Mumbai"
    end = "New York"

    print(f"All paths between: {start} and {end}: ",route_graph.get_paths(start,end))
    print(f"Shortest path between {start} and {end}: ", route_graph.get_shortest_path(start,end))    

    # path = []
    # path.append('ABC')

    # print(path)

    # path = []

    # path = path + ['ABC']
    # print(path)