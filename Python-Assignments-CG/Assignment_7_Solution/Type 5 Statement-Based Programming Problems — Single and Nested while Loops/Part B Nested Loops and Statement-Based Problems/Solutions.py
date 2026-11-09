# Q87. Print a Number Triangle
n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        print(j,end=" ")
        j+=1
    print()
    i+=1

# Q88. Print a Hollow Rectangle
r=int(input())
c=int(input())
i=1
while i<=r:
    j=1
    while j<=c:
        if i==1 or i==r or j==1 or j==c:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j+=1
    print()
    i+=1

# Q89. Print a Right-Aligned Triangle
n=int(input())
i=1
while i<=n:
    j=1
    while j<=n-i:
        print(" ",end=" ")
        j+=1
    j=1
    while j<=i:
        print("*",end=" ")
        j+=1
    print()
    i+=1

# Q90. Print a Multiplication Grid
n=int(input())
i=1
while i<=n:
    j=1
    while j<=n:
        print(i*j,end=" ")
        j+=1
    print()
    i+=1