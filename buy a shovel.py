k, r = input().split()
k = int(k)
r = int(r)

i = 1

while True:
    total = k * i
    
    # Check last digit
    if total % 10 == 0 or total % 10 == r:
        print(i)
        break
    
    i = i + 1
