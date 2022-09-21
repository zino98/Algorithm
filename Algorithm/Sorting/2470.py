import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()

right = n - 1
left = 0
answer = abs(data[left] + data[right])
final = [data[left], data[right]]

while(left < right):
  left_value = data[left]
  right_value = data[right]

  sum = left_value + right_value

  if(abs(sum) < answer):
    answer = abs(sum)
    final = [left_value, right_value]
    if answer == 0:
      break

  if sum < 0:
    left += 1
  else:
    right -= 1

print(final[0], final[1])