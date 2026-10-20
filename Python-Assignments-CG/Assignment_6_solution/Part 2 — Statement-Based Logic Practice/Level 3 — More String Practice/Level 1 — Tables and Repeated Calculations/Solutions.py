# Q96. Multiplication Tables from 1 to N
n=int(input())
k=int(input())
for i in range(1,n+1):
    for j in range(1,k+1):
        print(i,"x",j,"=",i*j)

# Q97. Number and Its Divisors
n=int(input())
for i in range(1,n+1):
    print(i,":",end=" ",sep="")
    for j in range(1,i+1):
        if i%j==0:
            print(j,end=" ")
    print()

# Q98. Count Divisors for Every Number
n=int(input())
for i in range(1,n+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    print(i,":",count)

# Q99. Perfect Numbers in a Range
n=int(input())
for i in range(1,n+1):
    total=0
    for j in range(1,i):
        if i%j==0:
            total+=j
    if total==i:
        print(i)

# Q100. Prime Numbers in a Range — Count Each Check
n=int(input())
for i in range(2,n+1):
    prime=True
    for j in range(2,i):
        if i%j==0:
            prime=False
            break
    if prime:
        print(i,end=" ")
print("Thank You")