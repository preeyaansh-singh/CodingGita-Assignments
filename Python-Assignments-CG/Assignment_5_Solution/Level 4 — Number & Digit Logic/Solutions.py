# Q23. Count Digits Using a Loop
num = int(input("Enter a number : "))
count = 0
for i in range(num):
    if num == 0:
        break
    count += 1
    num //= 10
print(count)

# Q24. Sum of Digits
number = abs(int(input()))
digit_sum = 0

for _ in range(number.bit_length()):
    if number <= 0:
        break
    digit_sum += number % 10
    number //= 10

print(digit_sum)

# Q25. Product of Digits
number = abs(int(input()))
digit_prod = 0

for _ in range(number.bit_length()):
    if number <= 0:
        break
    digit_prod *= number % 10
    number //= 10

print(digit_prod)

# Q26. Count Even Digits
number = abs(int(input("Enter a number : ")))
digit = 0
count = 0

for _ in range(number.bit_length()):
    if number <= 0:
        break
    digit = number % 10
    if digit % 2 == 0:
        count += 1
    number = number // 10

print(count)

# Q27. Sum of Even Digits
number = abs(int(input("Enter a number : ")))
digit = 0
count = 0

for _ in range(number.bit_length()):
    if number <= 0:
        break
    digit = number % 10
    if digit % 2 != 0:
        count += 1
    number = number // 10

print(count)

# Q28. Largest Digit Without max()
number = abs(int(input("Enter a number: ")))
greatest = 0

for _ in range(number):
    digit = number % 10
    if digit > greatest:
        greatest = digit
    number //= 10
    if number == 0:
        break

print(greatest)

# Q29. Smallest Digit Without min()
number = abs(int(input("Enter a number: ")))
smallest = 0

for _ in range(number):
    digit = number % 10
    if digit < smallest:
        greatest = digit
    number //= 10
    if number == 0:
        break

print(greatest)

# Q30. Reverse a Number
num = int(input("Enter a number : "))
new_num = 0

for i in range(num):
    if num == 0:
        break
    digit = num % 10
    new_num = new_num * 10 + digit
    num //= 10

print(new_num)

# Q31. Palindrome Number
num = int(input("Enter a number : "))
new_num = 0

for i in range(num):
    if num == 0:
        break
    digit = num % 10
    new_num = new_num * 10 + digit
    num //= 10
if new_num == num:
    print("Number is a pallindrome")
else:
    print("Number is not a pallindrome")

# Q32. Count a Specific Digit
num = int(input("Enter a number: "))
target = int(input("Enter target digit: "))
count = 0
if num == 0 and target == 0:
    count = 1
num = abs(num)
while num > 0:
    digit = num % 10
    if digit == target:
        count += 1
    num //= 10
print(count) 

# Q33. First Digit Using Repeated Division
num=int(input("Enter a number : "))
for i in range(num):
    if num<10:
        break
    num//=10
print(num)

# Q34. Difference Between Largest and Smallest Digit
num=int(input("Enter a number : "))
largest=0
smallest=9
while num>0:
    digit=num%10
    if digit>largest:
        largest=digit
    if digit<smallest:
        smallest=digit
    num//=10
print(largest-smallest)

# Q35. Digit Position Value
num=int(input("Emter a number : "))
position=1
while num>0:
    digit=num%10
    print(digit,position)
    num//=10
    position+=1

# Q36. Armstrong Number — 3 Digit
num=int(input("Enter a number : "))
temp=num
total=0
while temp>0:
    digit=temp%10
    total+=digit**3
    temp//=10
if total==num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")

    
