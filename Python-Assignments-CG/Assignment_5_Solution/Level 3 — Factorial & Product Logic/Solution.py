# Q15. Factorial of a Number
n = int(input("Enter a number : "))
fact = 1
for i in range (1,n+1):
    fact *= i 
print (fact)

# Q16. Factorial from 1 to N
num = int(input("Enter a number : "))
fact = 1
for i in range (1,num+1):
    fact *= i
    print(f"{i}! = {fact}")

# Q17. Product of Even Numbers
num = int(input("Enter a number : "))
prod = 1
for i in range (1, num+1):
    if i%2 == 0:
        prod *= i
print(prod)

# Q18. Product of Odd Numbers
num = int(input("Enter a number : "))
prod = 1
for i in range (1, num+1):
    if i%2 != 0:
        prod *= i
print(prod)

# Q19. Double Factorial — Even Numbers
num = int(input("Enter a number : "))
prod = 1
for i in range (2,num+1,2):
    prod *= i
print(prod)

# Q20. Sum of Squares
num = int(input("Enter a number : "))
sum = 0
for i in range (num+1):
    sum += i**2
print(sum)

# Q21. Sum of Cubes
num = int(input("Enter a number : "))
sum = 0
for i in range (num+1):
    sum += i**3
print(sum)

# Q22. Factorial-Based Sum
num = int(input("Enter a number : "))
count = 0
fact = 1
for i in range (1,num+1):
    fact *= i
    count += fact
print(count)

