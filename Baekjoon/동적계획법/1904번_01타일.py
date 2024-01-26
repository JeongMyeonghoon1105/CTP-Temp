memo = [0, 1, 2]

def f(n):
    if n <= 2:
        return n
    for i in range(3, n+1):
        memo.append((memo[i-1] + memo[i-2]) % 15746)
    return memo[n]

N = int(input())
print(f(N))
