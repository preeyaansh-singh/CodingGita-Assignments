# Q41. Count the Digits
n=int(input())
count=0
if n==0:
    count=1
while n>0:
    count+=1
    n//=10
print(count)

# Q42. Find the Sum of Digits
n=int(input())
total=0
while n>0:
    digit=n%10
    total+=digit
    n//=10
print(total)

# Q43. Reverse a Number
n=int(input())
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n//=10
print(reverse)

# Q44. Find the Product of Digits
n=int(input())
product=1
if n==0:
    product=0
while n>0:
    digit=n%10
    product*=digit
    n//=10
print(product)

# Q45. Print Digits from Right to Left
n=int(input())
while n>0:
    digit=n%10
    print(digit)
    n//=10