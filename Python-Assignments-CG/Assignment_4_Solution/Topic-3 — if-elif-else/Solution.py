# Q19. Grade Calculator
marks = int(input())
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
else:
    print("F")


# Q20. Temperature Category
temp = int(input())
if temp >= 40:
    print("Very Hot")
elif temp >= 30:
    print("Hot")
elif temp >= 20:
    print("Warm")
else:
    print("Cold")


# Q21. Traffic Signal
color = input().lower()
if color == "red":
    print("Stop")
elif color == "yellow":
    print("Wait")
elif color == "green":
    print("Go")
else:
    print("Invalid Signal")


# Q22. Electricity Usage Category
units = int(input())
if units <= 100:
    print("Low Usage")
elif units <= 300:
    print("Medium Usage")
elif units <= 500:
    print("High Usage")
else:
    print("Very High Usage")


# Q23. Movie Ticket Category
age = int(input())
if age < 5:
    print("Free Ticket")
elif age <= 12:
    print("Child Ticket")
elif age <= 59:
    print("Regular Ticket")
else:
    print("Senior Ticket")


# Q24. BMI Category
bmi = float(input())
if bmi < 18.5:
    print("Underweight")
elif bmi <= 24.9:
    print("Normal")
elif bmi <= 29.9:
    print("Overweight")
else:
    print("Obese")


# Q25. Month Days
month = int(input())
if month in [1, 3, 5, 7, 8, 10, 12]:
    print("31 Days")
elif month in [4, 6, 9, 11]:
    print("30 Days")
elif month == 2:
    print("28 or 29 Days")
else:
    print("Invalid Month")


# Q26. Simple Calculator
a = float(input())
b = float(input())
op = input()

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Invalid Operator")


# Q27. Day Number
day = int(input())
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid Day")


# Q28. Performance Level
score = int(input())
if score >= 90:
    print("Excellent")
elif score >= 75:
    print("Very Good")
elif score >= 60:
    print("Good")
elif score >= 40:
    print("Average")
else:
    print("Needs Improvement")