n = int(input())

count = 1  # At least one group exists
previous = input()

for i in range(n - 1):
    current = input()
    if current != previous:
        count += 1
    previous = current

print(count)
