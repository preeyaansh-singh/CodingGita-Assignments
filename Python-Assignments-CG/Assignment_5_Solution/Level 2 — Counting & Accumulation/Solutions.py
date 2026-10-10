# Q7. Sum of Numbers in a Range
start, end = map(int, input().split())

total = 0
for i in range(start, end + 1):
    total += i

print(total)


# Q8. Count Multiples of 3
N = int(input())

count = 0
for i in range(1, N + 1):
    if i % 3 == 0:
        count += 1

print(count)


# Q9. Sum of Multiples of 4
N = int(input())

total = 0
for i in range(1, N + 1):
    if i % 4 == 0:
        total += i

print(total)


# Q10. Count Numbers Divisible by Both 3 and 5
N = int(input())

count = 0
for i in range(1, N + 1):
    if i % 3 == 0 and i % 5 == 0:
        count += 1

print(count)


# Q11. Sum Numbers Except Multiples of 3
N = int(input())

total = 0
for i in range(1, N + 1):
    if i % 3 != 0:
        total += i

print(total)


# Q12. Count Even and Odd Together
N = int(input())

even = 0
odd = 0

for i in range(1, N + 1):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"Even = {even}, Odd = {odd}")


# Q13. Running Sum
N = int(input())

total = 0
for i in range(1, N + 1):
    total += i
    print(total)


# Q14. Running Product
N = int(input())

product = 1
for i in range(1, N + 1):
    product *= i
    print(product)