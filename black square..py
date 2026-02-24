# Read calories for strips
a = input().split()

a1 = int(a[0])
a2 = int(a[1])
a3 = int(a[2])
a4 = int(a[3])

# Read the string
s = input()

total = 0

for i in range(len(s)):
    if s[i] == '1':
        total = total + a1
    elif s[i] == '2':
        total = total + a2
    elif s[i] == '3':
        total = total + a3
    elif s[i] == '4':
        total = total + a4

print(total)
