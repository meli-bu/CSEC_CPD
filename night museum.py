s = input()

current = 'a'
rotations = 0

for i in range(len(s)):
    target = s[i]

    # clockwise distance
    cw = abs(ord(target) - ord(current))
    
    # minimum rotation (circle of 26 letters)
    step = min(cw, 26 - cw)

    rotations = rotations + step
    current = target   # move pointer

print(rotations)
