# PRINT A PATTERN
# 1
# 2 2
# 3 3 3 
# 4 4 4 4
# 5 5 5 5 5

a=int(input("ENTER YOUR RANGE:"))
for i in range(1,a):
    for j in range(0,i):
        print(i,end=" ")
    print()    