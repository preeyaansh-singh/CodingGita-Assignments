# Q9. Even or Odd
n = int(input())
if n % 2 == 0:
    print("Even")
else:
    print("Odd")


# Q10. Pass or Fail
marks = int(input())
if marks >= 40:
    print("Pass")
else:
    print("Fail")


# Q11. Adult or Minor
age = int(input())
if age >= 18:
    print("Adult")
else:
    print("Minor")


# Q12. Number Sign
n = int(input())
if n > 0:
    print("Positive")
else:
    print("Non-Positive")


# Q13. Divisible by 3
n = int(input())
if n % 3 == 0:
    print("Divisible by 3")
else:
    print("Not Divisible by 3")


# Q14. Login Password
correct_password = "python123"
password = input()
if password == correct_password:
    print("Login Successful")
else:
    print("Invalid Password")


# Q15. Username Check
username = input()
if username == "admin":
    print("Welcome Admin")
else:
    print("Invalid Username")


# Q16. Greater Between Two Numbers
a, b = map(int, input().split())
if a > b:
    print(a)
elif b > a:
    print(b)
else:
    print("Both are Equal")


# Q17. Hot or Comfortable
temp = int(input())
if temp > 30:
    print("Hot")
else:
    print("Comfortable")


# Q18. Shopping Discount Eligibility
amount = int(input())
if amount >= 5000:
    print("Discount Available")
else:
    print("No Discount")