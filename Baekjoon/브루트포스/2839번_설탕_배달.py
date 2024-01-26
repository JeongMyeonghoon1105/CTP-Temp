n = int(input())

f = n // 5

while f >= 0:
    if not (n - f * 5) % 3:
        t = (n - f * 5) // 3
        break
    f -= 1

if f < 0:
    print(-1)
else:
    print(f + t)
