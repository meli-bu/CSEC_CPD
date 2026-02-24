# Read number of wires
n = int(input())

# Read initial number of birds on each wire
birds = list(map(int, input().split()))

# Read number of shots
m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    wire_index = x - 1   # convert to 0-based index
    bird_index = y       # position of the bird (1-based)

    left = bird_index - 1       # birds to the left of the shot
    right = birds[wire_index] - bird_index  # birds to the right of the shot

    # Birds to the wire above (i-1), if it exists
    if wire_index - 1 >= 0:
        birds[wire_index - 1] += left

    # Birds to the wire below (i+1), if it exists
    if wire_index + 1 < n:
        birds[wire_index + 1] += right

    # Remove all birds from the current wire (shot bird dies, rest fly away)
    birds[wire_index] = 0

# Print final number of birds on each wire
for b in birds:
    print(b)
