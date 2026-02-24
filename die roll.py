from math import gcd

# Read Yakko's and Wakko's rolls
Y = int(input())
W = int(input())

# Maximum of the first two
max_roll = max(Y, W)

# Dot needs to roll at least max_roll
favorable = 6 - max_roll + 1
total = 6

# Reduce the fraction
g = gcd(favorable, total)

# Print result as irreducible fraction
print(f"{favorable//g}/{total//g}")
