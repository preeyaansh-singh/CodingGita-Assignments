# Q91. Print the Fibonacci Series up to a Limit
n=int(input())
a=0
b=1
if n>=0:
    print(0,end=" ")
while b<=n:
    print(b,end=" ")
    a,b=b,a+b
print()

# Q92. Print All Prime Numbers up to N
n=int(input())
i=2
while i<=n:
    j=2
    prime=True
    while j<i:
        if i%j==0:
            prime=False
            break
        j+=1
    if prime:
        print(i,end=" ")
    i+=1
print()

# Q93. Print All Armstrong Numbers up to N
n=int(input())
num=0
while num<=n:
    temp=num
    digits=0
    if temp==0:
        digits=1
    while temp>0:
        digits+=1
        temp//=10
    temp=num
    total=0
    while temp>0:
        digit=temp%10
        power=1
        i=1
        while i<=digits:
            power*=digit
            i+=1
        total+=power
        temp//=10
    if total==num:
        print(num,end=" ")
    num+=1
print()

# Q94. Print All Perfect Numbers up to N
n=int(input())
num=1
while num<=n:
    i=1
    total=0
    while i<num:
        if num%i==0:
            total+=i
        i+=1
    if total==num:
        print(num,end=" ")
    num+=1
print()

# Q95. Find All Pairs Whose Sum Is N
n=int(input())
a=1
while a<n-a:
    b=n-a
    print(a,"+",b)
    a+=1

# Q96. Print All Two-Digit Numbers with a Given Digit Sum
s=int(input())
num=10
while num<=99:
    first=num//10
    last=num%10
    if first+last==s:
        print(num,end=" ")
    num+=1
print()

# Q97. Find All Common Divisors of Two Numbers
a=int(input())
b=int(input())
i=1
while i<=a and i<=b:
    if a%i==0 and b%i==0:
        print(i,end=" ")
    i+=1
print()

# Q98. Find Prime Factor Pairs
n=int(input("Enter a number : "))
a=2
found=False
while a*a<=n:
    if n%a==0:
        b=n//a
        j=2
        prime_a=True
        while j<a:
            if a%j==0:
                prime_a=False
                break
            j+=1
        j=2
        prime_b=True
        while j<b:
            if b%j==0:
                prime_b=False
                break
            j+=1
        if prime_a and prime_b:
            print(a,"*",b)
            found=True
    a+=1
if not found:
    print("No prime factor pair")

print("Thank you")