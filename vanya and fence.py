n, h = map(int, input().split())
heights = list(map(int, input().split()))

print(sum(2 if x > h else 1 for x in heights))


