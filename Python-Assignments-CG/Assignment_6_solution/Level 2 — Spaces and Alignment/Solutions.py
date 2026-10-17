# Q13. Right-Aligned Half Pyramid
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)

# Q14. Inverted Right-Aligned Half Pyramid
n=int(input())
for i in range(n):
    print(" "*i+"*"*(n-i))

# Q15. Star Pyramid
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))

# Q16. Inverted Star Pyramid
n=int(input())
for i in range(n,0,-1):
    print(" "*(n-i)+"*"*(2*i-1))

# Q17. Solid Diamond
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))
for i in range(n-1,0,-1):
    print(" "*(n-i)+"*"*(2*i-1))

# Q18. Rhombus
n=int(input())
for i in range(n):
    print(" "*(n-i-1)+"*"*n)

# Q19. Mirrored Number Pattern
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print(" "*(2*(n-i)),end="")
    for j in range(i,0,-1):
        print(j,end="")
    print()

# Q20. Centered Number Pyramid
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end="")
        if j<i:
            print(" ",end="")
    print()

# Q21. Palindromic Number Pyramid
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")
    print()

# Q22. Alphabet Palindrome Pyramid
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(i):
        print(chr(65+j),end="")
    for j in range(i-2,-1,-1):
        print(chr(65+j),end="")
    print()

# Q23. Reverse-Starting Alphabet Triangle
n=int(input())
for i in range(n-1,-1,-1):
    for j in range(i,n):
        print(chr(65+j),end="")
        if j<n-1:
            print(" ",end="")
    print()