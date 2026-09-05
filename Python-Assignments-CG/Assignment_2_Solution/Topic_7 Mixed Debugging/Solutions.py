# mixed_debugging_answers.py
# Answers for Q56 - Q60 (Mixed Debugging + final challenge)
# Each section prints the corrected result and matches the expected outputs.

def q56_debug_student_program():
    # Corrected version of the buggy student program
    student_name = "Ravi"
    marks = "85"

    # convert marks to int before arithmetic
    total = int(marks) + 5

    print("Q56 — Debug the Student Program (fixed):")
    print("Student:", student_name)    # fixed variable name capitalization
    print("Marks:", total)
    print("Type:", type(total))
    print()

def q57_debug_number_program():
    # Original intention: print ones, tens, hundreds of 746
    number = 746

    ones = number % 10
    tens = (number // 10) % 10
    hundreds = number // 100

    print("Q57 — Debug the Number Program (fixed):")
    print("Ones:", ones)
    print("Tens:", tens)
    print("Hundreds:", hundreds)
    print()

def q58_debug_discount_program():
    # Fix: convert strings to numbers first
    price = "2000"
    discount = "15"

    price_num = float(price)
    discount_pct = float(discount)
    discount_amount = price_num * discount_pct / 100
    final_price = price_num - discount_amount

    print("Q58 — Debug the Discount Program (fixed):")
    print("Discount:", discount_amount)
    print("Final Price:", final_price)
    print()

def q59_complete_debugging_challenge():
    # Correct full program (fixed parsing, arithmetic, names, parentheses)
    student_name = "Rahul"
    marks1 = "85"
    marks2 = "90"
    marks3 = "78"

    m1 = int(marks1)
    m2 = int(marks2)
    m3 = int(marks3)

    total = m1 + m2 + m3
    average = total / 3

    print("Q59 — Complete Debugging Challenge (fixed):")
    print("Student:", student_name)
    print("Total Marks:", total)
    print("Average:", average)
    print("Marks Type:", type(total))
    print()

def q60_final_challenge_number_and_billing():
    # Part A — Number Analysis for number = 5836
    number = 5836
    ones = number % 10
    tens = (number // 10) % 10
    hundreds = (number // 100) % 10
    thousands = (number // 1000) % 10
    sum_digits = ones + tens + hundreds + thousands
    reversed_number = ones * 1000 + tens * 100 + hundreds * 10 + thousands

    print("Q60 — Part A: Number Analysis (number = 5836)")
    print("Thousands digit:", thousands)
    print("Hundreds digit:", hundreds)
    print("Tens digit:", tens)
    print("Ones digit:", ones)
    print("Sum of digits:", sum_digits)
    print("Reversed number:", reversed_number)
    print()

    # Part B — Product Billing
    price = "1250"
    quantity = "4"
    discount = "10"   # percent

    price_num = float(price)
    qty_num = int(quantity)
    discount_pct = float(discount)

    subtotal = price_num * qty_num
    discount_amount = subtotal * discount_pct / 100
    final_amount = subtotal - discount_amount

    print("Q60 — Part B: Product Billing")
    print("Subtotal:", subtotal)
    print("Discount amount:", discount_amount)
    print("Final amount:", final_amount)
    print()

if __name__ == "__main__":
    q56_debug_student_program()
    q57_debug_number_program()
    q58_debug_discount_program()
    q59_complete_debugging_challenge()
    q60_final_challenge_number_and_billing()

print("")