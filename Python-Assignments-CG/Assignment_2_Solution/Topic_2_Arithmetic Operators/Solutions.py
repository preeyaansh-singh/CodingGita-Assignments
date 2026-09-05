# arithmetic_answers.py
# Answers for Questions 11 — 20 (arithmetic operator exercises)

# --- Question 11: Basic Arithmetic ---
a = 20
b = 6
print("Q11 — Basic Arithmetic (a=20, b=6):")
print("Addition:         ", a + b)
print("Subtraction:      ", a - b)
print("Multiplication:   ", a * b)
print("Division (float): ", a / b)
print("Floor division:   ", a // b)
print("Remainder:        ", a % b)
print("Power (a ** b):   ", a ** b)
print()

# --- Question 12: Predict the Output ---
a = 17
b = 5
print("Q12 — Predict the Output (a=17, b=5):")
print("a / b  ->", a / b)   # float division
print("a // b ->", a // b)  # floor division
print("a % b  ->", a % b)   # remainder
print("Explanation: '/' gives true division (float). '//' gives integer quotient (floor). '%' gives leftover remainder.")
print()

# --- Question 13: Operator Precedence ---
result = 10 + 5 * 2
print("Q13 — Operator Precedence:")
print("10 + 5 * 2 =", result)
print("If you want addition first: (10 + 5) * 2 =", (10 + 5) * 2)
print()

# --- Question 14: More Precedence Practice ---
result = 20 - 4 * 3 + 2
print("Q14 — More Precedence Practice:")
print("20 - 4 * 3 + 2 =", result)
print("Make order explicit with parentheses: (20 - (4 * 3)) + 2 =", (20 - (4 * 3)) + 2)
print()

# --- Question 15: Power Operator ---
print("Q15 — Power Operator:")
print("2 ** 3 =", 2 ** 3)
print("3 ** 2 =", 3 ** 2)
print("10 ** 2 =", 10 ** 2)
side = 5
area_square = side ** 2
print("side = 5 -> area of square = side ** 2 =", area_square)
print()

# --- Question 16: Shopping Bill ---
notebook = 80
pen = 20
pencil = 10
total = notebook + pen + pencil
print("Q16 — Shopping Bill:")
print("Total Amount:", total)
print()

# --- Question 17: Multiple Quantities ---
notebook_price = 50
pen_price = 15
calc_price = 500
notebook_cost = 3 * notebook_price
pen_cost = 2 * pen_price
calc_cost = 1 * calc_price
total_bill = notebook_cost + pen_cost + calc_cost
print("Q17 — Multiple Quantities:")
print("Notebook Cost:    ", notebook_cost)
print("Pen Cost:         ", pen_cost)
print("Calculator Cost:  ", calc_cost)
print("Total Bill:       ", total_bill)
print()

# --- Question 18: Complete Groups and Remainder ---
students = 47
group_size = 5
complete_groups = students // group_size
students_left = students % group_size
print("Q18 — Complete Groups and Remainder:")
print("Complete Groups:", complete_groups)
print("Students Left:  ", students_left)
print()

# --- Question 19: Average Marks ---
python_marks = 85
math_marks = 78
physics_marks = 92
total_marks = python_marks + math_marks + physics_marks
average = total_marks / 3
print("Q19 — Average Marks:")
print("Total Marks:  ", total_marks)
print("Average Marks:", average)
print()

# --- Question 20: Percentage ---
eng = 78
math = 85
py = 92
phys = 81
chem = 74
total = eng + math + py + phys + chem
max_total = 5 * 100
percentage = (total / max_total) * 100
print("Q20 — Percentage:")
print("Total Marks: ", total, "/", max_total)
print("Percentage:  ", percentage, "%")
print()