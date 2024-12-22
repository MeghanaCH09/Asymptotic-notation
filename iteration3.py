def nthnum(n):
    iteration=0
    for i in range(0,n):
        for j in range(0,n):
            print("8", end=" ")
            iteration+=1
        print(" ")
    print("When the value of 'n' iteration is:", iteration)

nthnum(6)
nthnum(4)
nthnum(7)

print("With every n the time taken is n^2 (the time is doubled)")
print("(n^2)")