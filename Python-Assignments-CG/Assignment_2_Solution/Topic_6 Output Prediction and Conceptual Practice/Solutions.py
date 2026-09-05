# q51_55_answers.py
# Q51 - Q55: Predictions shown as actual outputs (type-casting, arithmetic, parentheses, digit extraction)

def q51_type_casting_output():
    a = "50"
    b = int(a)
    print("Q51 — Type Casting Output")
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    print()  # blank line

def q52_float_to_int():
    number = 99.99
    result = int(number)
    print("Q52 — Float to Integer")
    print(number)
    print(result)
    print("Note: int() truncates the decimal portion (does not round).")
    print()

def q53_arithmetic_output():
    a = 12
    b = 5
    print("Q53 — Arithmetic Output")
    print(a + b)   # addition
    print(a - b)   # subtraction
    print(a * b)   # multiplication
    print(a / b)   # true division (float)
    print(a // b)  # floor division
    print(a % b)   # remainder
    print()

def q54_parentheses_challenge():
    print("Q54 — Parentheses Challenge")
    print(10 + 5 * 2)        # multiplication before addition
    print((10 + 5) * 2)      # parentheses force addition first
    print(20 / 5 + 3)        # left-to-right after division
    print(20 / (5 + 3))      # parentheses change denominator
    print("Note: parentheses change evaluation order (operator precedence).")
    print()

def q55_digit_challenge():
    number = 684
    a = number % 10          # ones
    b = number // 10
    c = b % 10               # tens
    d = number // 100        # hundreds
    print("Q55 — Digit Challenge")
    print(a)   # ones
    print(c)   # tens
    print(d)   # hundreds
    print("Identification: a = ones, c = tens, d = hundreds.")
    print()

if __name__ == "__main__":
    q51_type_casting_output()
    q52_float_to_int()
    q53_arithmetic_output()
    q54_parentheses_challenge()
    q55_digit_challenge()
