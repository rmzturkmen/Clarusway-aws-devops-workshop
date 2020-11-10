# Draw Box

num = int(input("Please Enter box number: "))
i = 0
while i < num:  # rows
    j = 0
    while j < num:  # columns
        if i == 0 or i == num-1 or j == 0 or j == num-1:
            print("#", end=" ")
        else:
            print(" ", end=" ")
        j += 1
    i += 1
    print(" ")
