# Q29. College Admission Eligibility
marks = int(input())
attendance = int(input())
if marks >= 60 and attendance >= 75:
    print("Eligible")
else:
    print("Not Eligible")


# Q30. Scholarship Eligibility
marks = int(input())
income = int(input())
if marks >= 85 or income < 300000:
    print("Scholarship Available")
else:
    print("No Scholarship")


# Q31. Weekend Check
day = input()
if day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Weekday")


# Q32. Online Exam Access
username = input()
password = input()
if username == "student" and password == "python123":
    print("Access Granted")
else:
    print("Access Denied")


# Q33. Delivery Availability
city = input()
if city == "Ahmedabad" or city == "Gandhinagar":
    print("Delivery Available")
else:
    print("Delivery Unavailable")


# Q34. Number Range Check
num = int(input())
if 10 <= num <= 50:
    print("Inside Range")
else:
    print("Outside Range")


# Q35. Secure Transaction
amount = int(input())
otp = input()
if amount <= 50000 and otp == "1234":
    print("Transaction Approved")
else:
    print("Transaction Declined")


# Q36. Login with Role
username = input()
password = input()
if username == "admin":
    if password == "admin123":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")


# Q37. Driving License Eligibility
age = int(input())
status = input()
if age >= 18:
    if status == "pass":
        print("License Approved")
    else:
        print("Test Not Passed")
else:
    print("Age Not Eligible")


# Q38. ATM Withdrawal
balance = int(input())
withdraw = int(input())
if withdraw <= balance:
    if withdraw % 100 == 0:
        print("Withdrawal Successful")
    else:
        print("Enter Amount in Multiples of 100")
else:
    print("Insufficient Balance")


# Q39. Exam Result with Attendance
attendance = int(input())
marks = int(input())
if attendance >= 75:
    if marks >= 40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Not Eligible Due to Attendance")


# Q40. Bank Account Verification
account = input()
balance = int(input())
if account == "savings":
    if balance >= 1000:
        print("Minimum Balance Maintained")
    else:
        print("Minimum Balance Not Maintained")
else:
    print("Unsupported Account")


# Q41. Online Shopping Eligibility
amount = int(input())
payment = input()
if amount >= 500:
    if payment == "card":
        print("Card Payment Accepted")
    elif payment == "upi":
        print("UPI Payment Accepted")
    else:
        print("Unsupported Payment Method")
else:
    print("Minimum Order Amount Not Reached")


# Q42. Hostel Room Allocation
year = int(input())
attendance = int(input())
if year in [2, 3, 4]:
    if attendance >= 75:
        print("Room Eligible")
    else:
        print("Attendance Too Low")
else:
    print("Not Eligible by Year")


# Q43. Internet Plan Upgrade
plan = input()
usage = int(input())
if plan == "basic":
    if usage > 100:
        print("Recommend Upgrade")
    else:
        print("Basic Plan Is Sufficient")
else:
    print("Already on Higher Plan")