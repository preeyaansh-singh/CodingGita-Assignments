# Q43. Butterfly Pattern
n=int(input())
for i in range(1,n+1):
    print("*"*i+" "*(2*(n-i))+"*"*i)
for i in range(n-1,0,-1):
    print("*"*i+" "*(2*(n-i))+"*"*i)

# Q44. Hollow Hourglass
n=int(input())
for i in range(n):
    print(" "*i,end="")
    if i==0:
        print("*"*(2*n-1))
    elif i==n-1:
        print("*")
    else:
        print("*"+" "*(2*(n-i)-3)+"*")
for i in range(n-2,-1,-1):
    print(" "*i,end="")
    if i==0:
        print("*"*(2*n-1))
    else:
        print("*"+" "*(2*(n-i)-3)+"*")

# Q45. Alphabet Diamond
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(i):
        print(chr(65+j),end="")
    for j in range(i-2,-1,-1):
        print(chr(65+j),end="")
    print()
for i in range(n-1,0,-1):
    print(" "*(n-i),end="")
    for j in range(i):
        print(chr(65+j),end="")
    for j in range(i-2,-1,-1):
        print(chr(65+j),end="")
    print()

# Q46. Pascal's Triangle
n=int(input())
for i in range(n):
    print(" "*(n-i-1),end="")
    value=1
    for j in range(i+1):
        print(value,end=" ")
        value=value*(i-j)//(j+1)
    print()

# Q47. Heart Pattern
n=int(input())
for i in range(n//2):
    print(" "*(n//2-i-1)+"*"*(2*i+2)+" "*(n-2*i-2)+"*"*(2*i+2))
for i in range(n,0,-2):
    print(" "*((n-i)//2)+"*"*i)

# Q48. Hollow Heart
n=int(input())
for i in range(n//2):
    for j in range(2*n-1):
        if j==n//2-i-1 or j==n//2+i or j==3*n//2-i-1 or j==3*n//2+i:
            print("*",end="")
        else:
            print(" ",end="")
    print()
for i in range(n):
    for j in range(2*n-1):
        if j==i or j==2*n-2-i:
            print("*",end="")
        else:
            print(" ",end="")
    print()

# Q49. Star-and-Space Center Pattern
n=int(input())
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1 or i==n//2:
            print("*",end="")
        else:
            print(" ",end="")
    print()

# Q50. Custom Symbol Square
n=int(input())
symbol=input()
for i in range(n):
    print(symbol*n)

# Q51. User-Sized Hollow Rectangle
rows=int(input())
columns=int(input())
for i in range(rows):
    for j in range(columns):
        if i==0 or i==rows-1 or j==0 or j==columns-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()

# Q52. Create Your Own Pattern — Number Staircase
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end="")
    print()