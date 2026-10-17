# Q24. Increasing and Decreasing Star Triangle
n=int(input())
for i in range(1,n+1):
    print("*"*i)
for i in range(n-1,0,-1):
    print("*"*i)

# Q25. Number Hourglass
n=int(input())
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()
for i in range(2,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

# Q26. Alphabet Hourglass
n=int(input())
for i in range(n,0,-1):
    for j in range(i):
        print(chr(65+j),end="")
    print()
for i in range(2,n+1):
    for j in range(i):
        print(chr(65+j),end="")
    print()

# Q27. Alternating Star and Hash Grid
n=int(input())
for i in range(n):
    for j in range(n):
        if (i+j)%2==0:
            print("*",end="")
        else:
            print("#",end="")
    print()

# Q28. Binary Checkerboard
n=int(input())
for i in range(n):
    for j in range(n):
        if (i+j)%2==0:
            print(1,end="")
        else:
            print(0,end="")
    print()

# Q29. Multiplication Grid
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i*j,end=" ")
    print()

# Q30. Alternating-Direction Rows
n=int(input())
for i in range(1,n+1):
    if i%2!=0:
        for j in range(1,i+1):
            print(j,end="")
    else:
        for j in range(i,0,-1):
            print(j,end="")
    print()

# Q31. Number Diamond
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")
    print()
for i in range(n-1,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")
    print()

# Q32. Concentric Number Square
n=int(input())
size=2*n-1
for i in range(size):
    for j in range(size):
        value=n-min(i,j,size-1-i,size-1-j)
        print(value,end=" ")
    print()