size = int(input("Enter the size of the pattern:"))

i = 1
while i <= size:
    for i in range(1, size+1):
        print("*", end="")
    print()
    i = i+1