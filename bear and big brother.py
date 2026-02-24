a, b = input().split()

a = int(a)
b = int(b)

years = 0

while a <= b:
    a = a * 3
    b = b * 2
    years = years + 1

print(years)
