
# Q79. Check Whether a Number Is Prime

n = int(input())
i = 2
is_prime = True

if n <= 1:
    is_prime = False

while i < n:
    if n % i == 0:
        is_prime = False
        break
    i += 1

if is_prime:
    print("Prime")
else:
    print("Not Prime")


# Q80. Find HCF (GCD)

a = int(input())
b = int(input())

while b != 0:
    remainder = a % b
    a = b
    b = remainder

print(a)


# Q81. Find LCM

a = int(input())
b = int(input())

if a > b:
    lcm = a
else:
    lcm = b

while True:
    if lcm % a == 0 and lcm % b == 0:
        break
    lcm += 1

print(lcm)


# Q82. Check Whether a Number Is Perfect

n = int(input())

i = 1
total = 0

while i < n:
    if n % i == 0:
        total += i
    i += 1

if n > 1 and total == n:
    print("Perfect")
else:
    print("Not Perfect")


# Q83. Check Whether a Number Is Strong

n = int(input())

temp = n
total = 0

factorials = {
    0: 1, 1: 1, 2: 2, 3: 6, 4: 24,
    5: 120, 6: 720, 7: 5040,
    8: 40320, 9: 362880
}

while temp > 0:
    digit = temp % 10
    total += factorials[digit]
    temp //= 10

if total == n:
    print("Strong")
else:
    print("Not Strong")


# Q84. Check Whether a Number Is Armstrong

n = int(input())

temp = n
digits = 0

if temp == 0:
    digits = 1

while temp > 0:
    digits += 1
    temp //= 10

temp = n
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10

if total == n:
    print("Armstrong")
else:
    print("Not Armstrong")


# Q85. Convert Decimal to Binary

n = int(input())

binary = 0
place = 1

if n == 0:
    binary = 0

while n > 0:
    remainder = n % 2
    binary += remainder * place
    place *= 10
    n //= 2

print(binary)


# Q86. Find Sum of Divisors

n = int(input())

i = 1
total = 0

while i <= n:
    if n % i == 0:
        total += i
    i += 1

print(total)
