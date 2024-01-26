def find(h):
    for i in range(len(h)):
    # if h[i] >= over:
    #     break
        for j in range(9):
            # if h[j] >= over:
            #     break
            if h[i] + h[j] == over:
                h[i] = h[j] = 0
                return h

h = []

for i in range(9):
    h.append(int(input()))

h.sort()
s = sum(h)
over = s - 100

h = find(h)

for i in h:
    if i:
        print(i)
