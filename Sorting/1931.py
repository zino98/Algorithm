import sys
input = sys.stdin.readline

array = []
count = 1

n = int(input())
for i in range(n):
    [a,b] = map(int, input().split())
    array.append([a,b])
    
array.sort(key = lambda x:(x[1], x[0]))

end_time = array[0][1]
for i in range(1,n):
  if(array[i][0] >= end_time):
    count += 1
    end_time = array[i][1]

print(count)