# Q53. Second Largest Digit
num=int(input())
largest=-1
second=-1
for i in range(num.bit_lenght()):
    if num==0:
        break
    digit=num%10
    if digit>largest:
        second=largest
        largest=digit
    elif digit!=largest and digit>second:
        second=digit
    num//=10
print(second)

# Q54. Longest Consecutive Equal Character Run
s=input()
current=0
best=0
previous=""
for ch in s:
    if ch==previous:
        current+=1
    else:
        current=1
    if current>best:
        best=current
    previous=ch
print(best)

# Q55. Most Frequent Character — Controlled Approach
s=input()
target=input()
count=0
for ch in s:
    if ch==target:
        count+=1
frequency=count/len(s)*100 if len(s)>0 else 0
print(f"Count = {count}, Frequency = {round(frequency,2)}%")

# Q56. Running Digit Sum Until the End
num=int(input())
total=0
while num>0:
    total+=num%10
    print(total)
    num//=10

# Q57. Number with Most Even Digits
num=int(input())
even=0
odd=0
while num>0:
    digit=num%10
    if digit%2==0:
        even+=1
    else:
        odd+=1
    num//=10
if even>odd:
    print("More Even Digits")
elif odd>even:
    print("More Odd Digits")
else:
    print("Equal")

# Q58. Alternating Digit Sum
num=int(input())
total=0
sign=1
for i in range(10):
    if num==0:
        break
    digit=num%10
    total+=digit*sign
    sign*=-1
    num//=10
print(total)

# Q59. Output Prediction — Accumulator Trap
total=0
for i in range(1,6):
    total=total+i*2
    print(total)
# Output:
# 2
# 6
# 12
# 20
# 30

# Q60. Output Prediction — Condition Inside Loop
count=0
for i in range(1,11):
    if i%2==0:
        count=count+1
print(count)
# Output: 5
# Explanation: There are 5 even numbers from 1 to 10:
# 2, 4, 6, 8, 10. The count increases once for each.

# Q61. Debug the Accumulator
# Mistake: sum=i replaces the previous value instead of adding to it.
total=0
for i in range(1,6):
    total+=i
print(total)
# Output: 15
# Explanation: The accumulator stores the previous total and adds i
# in every iteration: 1, 3, 6, 10, 15.