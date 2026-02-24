username = input().strip()

# Find number of distinct characters
distinct_characters = set(username)

# Check if count is even or odd
if len(distinct_characters) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
