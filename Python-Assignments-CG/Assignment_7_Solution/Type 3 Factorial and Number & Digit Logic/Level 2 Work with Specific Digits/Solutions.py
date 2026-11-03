# Q46. Find the First and Last Digit
n=int(input())
last=n%10
while n>=10:
    n//=10
first=n
print("First digit:",first)
print("Last digit:",last)

# Q47. Count Even Digits
n=int(input())
count=0
if n==0:
    count=1
while n>0:
    digit=n%10
    if digit%2==0:
        count+=1
    n//=10
print(count)

# Q48. Count Odd Digits
n=int(input())
count=0
while n>0:
    digit=n%10
    if digit%2!=0:
        count+=1
    n//=10
print(count)

# Q49. Find the Sum of Even Digits
n=int(input())
total=0
while n>0:
    digit=n%10
    if digit%2==0:
        total+=digit
    n//=10
print(total)

# Q50. Find the Largest Digit
n=int(input())
largest=0
while n>0:
    digit=n%10
    if digit>largest:
        largest=digit
    n//=10
print(largest)

# Q51. Find the Smallest Digit
n=int(input())
smallest=9
if n==0:
    smallest=0
while n>0:
    digit=n%10
    if digit<smallest:
        smallest=digit
    n//=10
print(smallest)