class graph:

    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
# Check for the visisted and unvisited nodes
'''
algorithm starts at the root node (selecting some arbitrary node as the root node 
in the case of a graph) and explores as far as possible along each branch 
before backtracking.

recursive function takes the graph and the start node and 
initially visited node is None
if visited node is none, start is visited
else for next node in graph excluding the visited one 
do the recursive function again
'''
def dfs(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        print(visited,graph[start]-visited)
        dfs(graph, next, visited)
    return visited

gdict = { "a" : set(["b","c"]),
                "b" : set(["a", "d"]),
                "c" : set(["a", "d"]),
                "d" : set(["e"]),
                "e" : set(["a"])
                }


dfs(gdict, 'a')