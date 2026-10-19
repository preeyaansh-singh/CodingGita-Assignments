# Q53. Number Increasing Reverse Pyramid
n=int(input())
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

# Q54. Square Fill Pattern
n=int(input())
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()

# Q55. Left Half Pyramid
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))

# Q56. Reverse Right Half Pyramid
n=int(input())
for i in range(n,0,-1):
    print("*"*i)

# Q57. Left Half Pyramid — Increasing
n=int(input())
for i in range(1,n+1):
    print("*"*i)

# Q58. Reverse Left Half Pyramid
n=int(input())
for i in range(n):
    print(" "*i+"*"*(n-i))

# Q59. Triangle Star Pattern
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)

# Q60. Mirror-Image Number Triangle
n=int(input())
for i in range(1,n+1):
    print(" "*(i-1),end="")
    for j in range(i,n+1):
        print(j,end="")
        if j<n:
            print(" ",end="")
    print()

# Q61. Hollow Reverse Triangle
n=int(input())
for i in range(n):
    print(" "*i,end="")
    for j in range(n-i):
        if i==0 or j==0 or j==n-i-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()

# Q62. Hollow Diamond Pyramid
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i),end="")
    if i==1:
        print("*")
    else:
        print("*"+" "*(2*i-3)+"*")
for i in range(n-1,0,-1):
    print(" "*(n-i),end="")
    if i==1:
        print("*")
    else:
        print("*"+" "*(2*i-3)+"*")

# Q63. Hollow Hourglass Pattern
n=int(input())
for i in range(n):
    print(" "*i,end="")
    if i==n-1:
        print("*")
    else:
        print("*"+" "*(2*(n-i)-3)+"*")
for i in range(n-2,-1,-1):
    print(" "*i+"*"+" "*(2*(n-i)-3)+"*")

# Q64. Right Pascal's Triangle
n=int(input())
for i in range(1,n+1):
    print("*"*i)
for i in range(n-1,0,-1):
    print("*"*i)

# Q65. Pattern Size Challenge
# Example: Test the star pyramid with N = 3, 5 and 7.
for n in (3,5,7):
    print("N =",n)
    for i in range(1,n+1):
        print(" "*(n-i)+"*"*(2*i-1))
    print()