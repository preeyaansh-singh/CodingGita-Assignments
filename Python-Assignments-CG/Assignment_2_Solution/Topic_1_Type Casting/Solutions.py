# type_conversions_answers.py
# Answers for Questions 1 — 10 (conversion exercises)

# --- Question 1: String to Integer ---
age = "25"
age_int = int(age)
print("Q1:")
print(age_int)
print(type(age_int))
print()  # blank line

# --- Question 2: String to Float ---
marks = "75.5"
marks_float = float(marks)
print("Q2:")
print(marks_float)
print(type(marks_float))
print()

# --- Question 3: Integer to Float ---
number = 50
number_float = float(number)
print("Q3:")
print(number_float)
print(type(number_float))
print()

# --- Question 4: Float to Integer ---
marks = 85.9
marks_int = int(marks)   # decimal part will be truncated
print("Q4:")
print(marks_int)
print(type(marks_int))
print()  # note: decimal part .9 is dropped (truncated)

# --- Question 5: Integer to String ---
roll_number = 101
roll_str = str(roll_number)
print("Q5:")
print(roll_str)
print(type(roll_str))
print()

# --- Question 6: Multiple Conversions ---
v1 = int("18")
v2 = float("92.5")
v3 = str(100)
v4 = int(45.8)   # decimal truncated -> 45
print("Q6:")
print(v1, type(v1))
print(v2, type(v2))
print(v3, type(v3))
print(v4, type(v4))
print()

# --- Question 7: Predict the Output (then run it) ---
print("Q7 (predicted):")
print("b -> 20")
print("d -> 10")
print("f -> '25'")
print("types -> <class 'int'>, <class 'int'>, <class 'str'>")
print()
# Now actual code:
a = "20"
b = int(a)

c = 10.8
d = int(c)

e = 25
f = str(e)

print("Q7 (actual run):")
print(b)
print(d)
print(f)
print(type(b))
print(type(d))
print(type(f))
print()

# --- Question 8: Debug Type Casting ---
# Original buggy code:
# age = "19"
# new_age = age + 1   # error: can't add int to str
# Correct version:
age = "19"
new_age = int(age) + 1
print("Q8:")
print("Age:", new_age)
print()

# --- Question 9: Marks Conversion ---
marks = "85"
final_marks = int(marks) + 5
print("Q9:")
print("Final Marks:", final_marks)
print()

# --- Question 10: Price Conversion ---
price = "1499.50"
total_amount = float(price) + 99.50
print("Q10:")
print("Total Amount:", total_amount)
print()