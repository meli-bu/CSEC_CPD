s = input().strip()

# Count uppercase and lowercase letters
upper_count = 0
lower_count = 0

for ch in s:
    if ch.isupper():
        upper_count += 1
    else:
        lower_count += 1

# Apply the rule
if upper_count > lower_count:
    print(s.upper())
else:
    print(s.lower())
