n = 3  # Number of rows

for i in range(1, n + 2):
    for j in range(n - i + 1):
        print("  ", end="")
    for j in range(i):
        print("*", end="     ")
    print()
