# a, b, c = map(int, input().split())
# power = 1
# count = 0

# save = [False]

# if a < c:
#   pass
# else:
#   while True:
#     power = (power * a) % c
#     save.append(power)

#     # print(save)

#     if count != 0 and save[1] == power:
#       # print(count)
#       print(save[b % count + 2])
#       break

#     count += 1

# a, b, c = map(int, input().split())
# save = [1]
# power = 1
# count = 0

# while a < c:
#   a *= 2
#   count += 1
#   save.append(a % c)

# pivot = count

# while True:
#   power = (power * a) % c
#   save.append(power)

#   print(save)

#   # if count != 0 and save[1] == power:
#   if count != pivot and save[pivot] == power:
#     # print(count)
#     print(save[pivot + b % (count - pivot)] % c)
#     break

#   count += 1

def pow(base, expo, modular):
  if expo == 1:
    return base % modular
  elif expo % 2 == 1:
    return (base * pow(base, expo-1, modular)) % modular
  else:
    return (pow(base, expo // 2, modular) * pow(base, expo // 2, modular)) % modular

a, b, c = map(int, input().split())
print(pow(a, b, c))
