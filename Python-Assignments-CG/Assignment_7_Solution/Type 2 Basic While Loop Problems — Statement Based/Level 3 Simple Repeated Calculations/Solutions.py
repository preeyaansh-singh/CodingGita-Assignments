# Q31. Calculate the Total Cost
price=int(input())
quantity=int(input())
total=0
i=1
while i<=quantity:
    total+=price
    i+=1
print(total)

# Q32. Calculate Total Savings
daily_saving=int(input())
days=int(input())
total=0
i=1
while i<=days:
    total+=daily_saving
    i+=1
print(total)

# Q33. Calculate a Number Raised to a Power
base=int(input())
power=int(input())
result=1
i=1
while i<=power:
    result*=base
    i+=1
print(result)

# Q34. Calculate Factorial
n=int(input())
factorial=1
i=1
while i<=n:
    factorial*=i
    i+=1
print(factorial)

# Q35. Find the Sum from START to END
start=int(input())
end=int(input())
total=0
while start<=end:
    total+=start
    start+=1
print(total)