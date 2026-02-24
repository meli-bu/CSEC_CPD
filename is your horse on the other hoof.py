# Read the colors of the four horseshoes
s1 = int(input())
s2 = int(input())
s3 = int(input())
s4 = int(input())

# Store them in a list
shoes = [s1, s2, s3, s4]

# Use a set to count unique colors
unique_colors = set(shoes)

# Minimum horseshoes to buy = 4 minus the number of unique colors
to_buy = 4 - len(unique_colors)

print(to_buy)
