from cs50 import get_int

while True:
    height = get_int("Height: ")
    if height >= 1 and height <= 8:
        break
for line in range(height):
    for space in range(1, height-line, +1):
        print(" ", end="")
    for thorp in range(line+1):
        print("#", end="")
    print("\n", end="")