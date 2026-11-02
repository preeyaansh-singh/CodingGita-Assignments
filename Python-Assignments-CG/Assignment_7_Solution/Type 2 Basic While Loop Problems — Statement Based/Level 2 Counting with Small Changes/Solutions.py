# Q26. Multiplication Table
n=int(input())
i=1
while i<=10:
    print(n,"x",i,"=",n*i)
    i+=1

# Q27. Count by a Given Step
start=int(input())
step=int(input())
i=1
while i<=5:
    print(start)
    start+=step
    i+=1

# Q28. Sum of Numbers from 1 to N
n=int(input())
i=1
total=0
while i<=n:
    total+=i
    i+=1
print(total)

# Q29. Sum of Even Numbers up to N
n=int(input())
i=2
total=0
while i<=n:
    total+=i
    i+=2
print(total)

# Q30. Sum of Odd Numbers up to N
n=int(input())
i=1
total=0
while i<=n:
    total+=i
    i+=2
print(total)