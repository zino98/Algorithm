import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
  x,y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

visited = [0] * n

def bfs(graph, start, visited):
  visited[start] = 1
  for i in graph[start]:
    if(visited[i] == 0):
      bfs(graph,i,visited)

  return True

bfs(graph,1,visited)
print(sum(visited) - 1)