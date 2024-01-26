n = int(input())
lst = list(map(int, input().split()))
lst.sort()

memo = [0 for i in range(n)]
i = 0
while i < n:
  if i == 0:
    memo[i] = lst[i]
  else:
    memo[i] = memo[i-1] + lst[i]
  i += 1

print(sum(memo))
