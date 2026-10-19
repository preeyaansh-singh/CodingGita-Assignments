# Q33. Hollow Square
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()

# Q34. Hollow Rectangle
rows=int(input())
columns=int(input())
for i in range(rows):
    for j in range(columns):
        if i==0 or i==rows-1 or j==0 or j==columns-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()

# Q35. Hollow Number Square
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print(1,end="")
        else:
            print(0,end="")
    print()

# Q36. Hollow Right-Angled Triangle
n=int(input())
for i in range(n):
    for j in range(i+1):
        if j==0 or j==i or i==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()

# Q37. Hollow Inverted Triangle
n=int(input())
for i in range(n,0,-1):
    for j in range(i):
        if i==n or j==0 or j==i-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()

# Q38. Hollow Pyramid
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(2*i-1):
        if i==n or j==0 or j==2*i-2:
            print("*",end="")
        else:
            print(" ",end="")
    print()

# Q39. Hollow Diamond
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(2*i-1):
        if j==0 or j==2*i-2:
            print("*",end="")
        else:
            print(" ",end="")
    print()
for i in range(n-1,0,-1):
    print(" "*(n-i),end="")