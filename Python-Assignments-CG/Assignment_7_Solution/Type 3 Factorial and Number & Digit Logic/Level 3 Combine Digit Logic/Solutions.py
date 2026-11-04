# Q52. Check Whether a Number Is a Palindrome
n=int(input())
temp=n
reverse=0
while temp>0:
    digit=temp%10
    reverse=reverse*10+digit
    temp//=10
if n==reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")

# Q53. Count How Many Times a Digit Appears
n=int(input())
d=int(input())
count=0
if n==0 and d==0:
    count=1
while n>0:
    digit=n%10
    if digit==d:
        count+=1
    n//=10
print(count)

# Q54. Check Whether All Digits Are the Same
n=int(input())
digit=n%10
same=True
while n>0:
    current=n%10
    if current!=digit:
        same=False
    n//=10
if same:
    print("Yes")
else:
    print("No")

# Q55. Compare the Sum of First and Last Digits with the Middle Digits' Sum
n=int(input())
last=n%10
temp=n
middle_sum=0
while temp>=10:
    digit=temp%10
    middle_sum+=digit
    temp//=10
first=temp
middle_sum-=last
print("First and last digits sum:",first+last)
print("Middle digits sum:",middle_sum)