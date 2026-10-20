# Q66. Count Digits
n=abs(int(input()))
count=0
if n==0:
    count=1
while n>0:
    count+=1
    n//=10
print(count)

# Q67. Sum of Digits
n=abs(int(input()))
total=0
while n>0:
    total+=n%10
    n//=10
print(total)

# Q68. Product of Digits
n=abs(int(input()))
product=1
if n==0:
    product=0
while n>0:
    product*=n%10
    n//=10
print(product)

# Q69. Reverse a Number
n=int(input())
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n//=10
print(reverse)

# Q70. Palindrome Number
n=int(input())
original=n
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n//=10
print(original==reverse)

# Q71. Prime Number
n=int(input())
prime=True
if n<2:
    prime=False
else:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            prime=False
            break
print(prime)

# Q72. Primes from 1 to N
n=int(input())
for num in range(2,n+1):
    prime=True
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            prime=False
            break
    if prime:
        print(num,end=" ")
print()

# Q73. First N Fibonacci Numbers
n=int(input())
a=0
b=1
for i in range(n):
    print(a,end=" ")
    c = a+b
    a = b
    b = c
print()

# Q74. GCD of Two Numbers
a=int(input())
b=int(input())
gcd=1
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        gcd=i
print(gcd)

# Q75. LCM of Two Numbers
a=int(input())
b=int(input())
lcm=a if a>b else b
while True:
    if lcm%a==0 and lcm%b==0:
        print(lcm)
        break
    lcm+=1