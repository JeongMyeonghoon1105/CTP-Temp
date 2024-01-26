n, m = map(int, input().split())

never_seen = []
never_heard_of = []
answer = []

for i in range(n):
    never_seen.append(input())

for i in range(m):
    never_heard_of.append(input())

never_seen.sort()
never_heard_of.sort()

s = 0
h = 0

while True:
    if never_seen[s][0] < never_heard_of[h][0]:
        s += 1 
    elif never_seen[s][0] == never_heard_of[h][0]:
        pass
    else:
        while h < len(never_heard_of) and never_seen[s][0] != never_heard_of[h][0]:
            h += 1
        if h == len(never_heard_of):
            s += 1

print(len(answer))
for i in answer:
    print(i)
