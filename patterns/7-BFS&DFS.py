graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = []   # List to keep track of visited nodes.
queue = []     # Initialize a queue

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        s = queue.pop(0) 
        print (s, end = " ") 
        
        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.append(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)


# Driver Code
bfs(visited, graph, 'A')
dfs(visited, graph, 'A')