import sys

input = sys.stdin.readline

n = int(input())

for j in range(n):
  array = []
  t = int(input())
  for i in range(t):
    [a,b] = map(int, input().split())
    array.append([a,b])
    
  array.sort()

  cnt = 1
  N = array[0][1]

  for v in range(1,t):
    if(array[v][1] < N):
      N = array[v][1]
      cnt += 1

  print(cnt)