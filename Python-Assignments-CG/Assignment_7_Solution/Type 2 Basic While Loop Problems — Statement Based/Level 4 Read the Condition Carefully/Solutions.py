# Q36. Count Down by Two
n=int(input())
while n>=2:
    print(n)
    n-=2

# Q37. Repeatedly Divide by Two
n=int(input())
while n>0:
    n//=2
    print(n)

# Q38. Count How Many Steps Are Needed
n=int(input())
steps=0
while n>0:
    n-=3
    steps+=1
print(steps)

# Q39. Save Until the Target Is Reached
saved=int(input())
daily_amount=int(input())
target=int(input())
days=0
while saved<target:
    saved+=daily_amount
    days+=1
print(days)

# Q40. Print a Number Sequence in Reverse Steps
start=int(input())
step=int(input())
while start>=0:
    print(start)
    start-=step