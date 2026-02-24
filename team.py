n = int(input())

count = 0

for i in range(n):
    a, b, c = input().split()
    
    a = int(a)
    b = int(b)
    c = int(c)
    
    if a + b + c >= 2:
        count += 1

print(count)
