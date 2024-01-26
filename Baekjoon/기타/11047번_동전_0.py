values = []

def find(k, count):
  pivot = 0
  while k > 0:
    # print('k : ', k)
    if count == 0:
      i = 0
      while i < len(values) and values[i] <= k:
        i += 1
      pivot = i-1
    else:
      i = pivot
      while i > 0 and values[i] > k:
        i -= 1
      pivot = i
    k -= values[pivot]
    count += 1
  return count

n, k = map(int, input().split())

for i in range(n):
  values.append(int(input()))

print(find(k, 0))
