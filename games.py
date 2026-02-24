n = int(input())

home = []
guest = []

for i in range(n):
    colors = input().split()
    home.append(int(colors[0]))
    guest.append(int(colors[1]))

count = 0

# Check every pair (i host, j guest)
for i in range(n):
    for j in range(n):
        if i != j:
            if home[i] == guest[j]:
                count += 1

print(count)
