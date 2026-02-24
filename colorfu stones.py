# Read number of stones
n = int(input())
s = input()  # string of colors

# Count minimum stones to remove
count = 0

for i in range(1, n):
    if s[i] == s[i-1]:  # same color as previous
        count += 1

print(count)
