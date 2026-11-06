# Q56. Print Factorial Values from 1! to N!
n=int(input())
i=1
factorial=1
while i<=n:
    factorial*=i
    print(factorial)
    i+=1

# Q57. Check Whether a Number Is a Factorial Value
n=int(input())
i=1
factorial=1
found=False
while factorial<=n:
    if factorial==n:
        found=True
    i+=1
    factorial*=i
if found:
    print("Yes")
else:
    print("No")

# Q58. Find the Largest Factorial Not Greater Than N
n=int(input())
i=1
factorial=1
while factorial<=n:
    result=factorial
    i+=1
    factorial*=i
print(result)