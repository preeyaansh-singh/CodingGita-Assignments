# type_casting_arithmetic_answers.py
# Solutions for Questions 45 - 50

def q45_string_numbers():
    price = "1200"
    quantity = "4"
    price_num = int(price)
    qty_num = int(quantity)
    total_price = price_num * qty_num
    print("Q45 — String Numbers:")
    print("Price:", price_num)
    print("Quantity:", qty_num)
    print("Total Price:", total_price)
    print()

def q46_student_result():
    python_marks = "85"
    math_marks = "78"
    physics_marks = "91"
    py = int(python_marks)
    ma = int(math_marks)
    ph = int(physics_marks)
    total = py + ma + ph
    average = total / 3
    print("Q46 — Student Result:")
    print("Total Marks:", total)
    print("Average Marks:", average)
    print()

def q47_bill_with_tax():
    price = "1500"
    quantity = "2"
    tax_rate = "5"
    price_num = float(price)
    qty_num = int(quantity)
    tax_pct = float(tax_rate)
    subtotal = price_num * qty_num
    tax_amount = subtotal * tax_pct / 100
    final_bill = subtotal + tax_amount
    print("Q47 — Bill with Tax:")
    print("Subtotal:", subtotal)
    print("Tax amount:", tax_amount)
    print("Final bill:", final_bill)
    print()

def q48_discount_and_gst():
    price = 2000.0
    discount_pct = 15.0
    gst_pct = 18.0
    discount_amount = price * discount_pct / 100
    price_after_discount = price - discount_amount
    gst_amount = price_after_discount * gst_pct / 100
    final_price = price_after_discount + gst_amount
    print("Q48 — Discount + GST:")
    print("Discount amount:", discount_amount)
    print("Price after discount:", price_after_discount)
    print("GST amount:", gst_amount)
    print("Final price:", final_price)
    print()

def q49_debug_billing_program():
    # Buggy original:
    # price = "500"
    # quantity = 3
    # total = price + quantity            # wrong: string + int, also should multiply
    # Corrected version:
    price = "500"
    quantity = 3
    price_num = int(price)
    total = price_num * quantity
    print("Q49 — Debug the Billing Program (fixed):")
    print("Total:", total)
    print()

def q50_debug_marks_program():
    # Buggy original:
    # marks1 = "80"
    # marks2 = "75"
    # marks3 = "90"
    # total = marks1 + marks2 + marks3   # wrong: string concatenation
    # Corrected:
    marks1 = "80"
    marks2 = "75"
    marks3 = "90"
    m1 = int(marks1)
    m2 = int(marks2)
    m3 = int(marks3)
    total = m1 + m2 + m3
    print("Q50 — Debug the Marks Program (fixed):")
    print("Total Marks:", total)
    print()

if __name__ == "__main__":
    q45_string_numbers()
    q46_student_result()
    q47_bill_with_tax()
    q48_discount_and_gst()
    q49_debug_billing_program()
    q50_debug_marks_program()