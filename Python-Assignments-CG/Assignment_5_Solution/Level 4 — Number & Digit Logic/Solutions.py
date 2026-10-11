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
greatest = 0

for _ in range(number):
    digit = number % 10
    if digit < greatest:
        greatest = digit
    number //= 10
    if number == 0:
        break

print(greatest)



    
   


