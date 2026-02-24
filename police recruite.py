n = int(input())
events = input().split()

officers = 0
untreated = 0

for i in range(n):
    event = int(events[i])

    if event == -1:
        if officers > 0:
            officers = officers - 1
        else:
            untreated = untreated + 1
    else:
        officers = officers + event

print(untreated)
