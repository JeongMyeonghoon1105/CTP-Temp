import sys

def binary_search(lst, key):
  start = 0
  end = len(lst) - 1

  while start <= end:
    mid = (start + end) // 2
    if key == lst[mid]:
      return 1
    elif key > lst[mid]:
      start = mid + 1
    else:
      end = mid - 1
  
  return 0

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
a.sort()

m = int(input())
search = list(map(int, sys.stdin.readline().split()))

for i in search:
  print(binary_search(a, i))
