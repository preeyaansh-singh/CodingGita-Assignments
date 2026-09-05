# digit_extraction_answers.py
# Answers for Q21 - Q35 (digit extraction problems)
# Uses only arithmetic (% and //) for digit extraction.

def q21_ones_digit():
    number = 583
    ones = number % 10
    print("Q21 — Ones Digit:")
    print("Ones Digit:", ones)
    print()

def q22_tens_digit():
    number = 583
    tens = (number // 10) % 10
    print("Q22 — Tens Digit:")
    print("Tens Digit:", tens)
    print()

def q23_hundreds_digit():
    number = 583
    hundreds = (number // 100) % 10  # or number // 100
    print("Q23 — Hundreds Digit:")
    print("Hundreds Digit:", hundreds)
    print()

def q24_three_digit_analyzer():
    number = 746
    ones = number % 10
    tens = (number // 10) % 10
    hundreds = (number // 100) % 10
    print("Q24 — Three-Digit Number Analyzer (number = 746):")
    print("Ones Digit:", ones)
    print("Tens Digit:", tens)
    print("Hundreds Digit:", hundreds)
    print()

def q25_four_digit_number():
    number = 5829
    ones = number % 10
    tens = (number // 10) % 10
    hundreds = (number // 100) % 10
    thousands = (number // 1000) % 10
    print("Q25 — Four-Digit Number (number = 5829):")
    print("Ones Digit:", ones)
    print("Tens Digit:", tens)
    print("Hundreds Digit:", hundreds)
    print("Thousands Digit:", thousands)
    print()

def q26_sum_of_digits():
    number = 583
    ones = number % 10
    tens = (number // 10) % 10
    hundreds = (number // 100) % 10
    total = ones + tens + hundreds
    print("Q26 — Sum of Digits (number = 583):")
    print("Sum of Digits:", total)
    print()

def q27_four_digit_sum():
    number = 4726
    ones = number % 10
    tens = (number // 10) % 10
    hundreds = (number // 100) % 10
    thousands = (number // 1000) % 10
    total = ones + tens + hundreds + thousands
    print("Q27 — Four-Digit Sum (number = 4726):")
    print("Sum of Digits:", total)
    print()

def q28_product_of_digits():
    number = 234
    ones = number % 10
    tens = (number // 10) % 10
    hundreds = (number // 100) % 10
    product = ones * tens * hundreds
    print("Q28 — Product of Digits (number = 234):")
    print("Product of Digits:", product)
    print()

def q29_reverse_three_digit():
    number = 583
    ones = number % 10
    tens = (number // 10) % 10
    hundreds = (number // 100) % 10
    reversed_num = ones * 100 + tens * 10 + hundreds
    print("Q29 — Reverse a Three-Digit Number:")
    print("Original Number:", number)
    print("Reversed Number:", reversed_num)
    print()

def q30_reverse_four_digit():
    number = 4726
    ones = number % 10
    tens = (number // 10) % 10
    hundreds = (number // 100) % 10
    thousands = (number // 1000) % 10
    reversed_num = ones * 1000 + tens * 100 + hundreds * 10 + thousands
    print("Q30 — Reverse a Four-Digit Number:")
    print("Original Number:", number)
    print("Reversed Number:", reversed_num)
    print()

def q31_place_value():
    number = 5834
    thousands_digit = (number // 1000) % 10
    hundreds_digit = (number // 100) % 10
    tens_digit = (number // 10) % 10
    ones_digit = number % 10
    print("Q31 — Place Value (number = 5834):")
    print("Thousands Place:", thousands_digit * 1000)
    print("Hundreds Place:", hundreds_digit * 100)
    print("Tens Place:", tens_digit * 10)
    print("Ones Place:", ones_digit)
    print()

def q32_difference_first_last():
    number = 583
    hundreds = (number // 100) % 10
    ones = number % 10
    diff = hundreds - ones
    print("Q32 — Difference Between First and Last Digit (number = 583):")
    print("Difference:", diff)
    print()

def q33_debug_digit_extraction():
    # buggy code:
    # number = 583
    # ones = number / 10   # wrong: / gives float and is not last digit
    # print("Ones Digit:", ones)
    # Correct version:
    number = 583
    ones = number % 10
    print("Q33 — Debug Digit Extraction (fixed):")
    print("Ones Digit:", ones)
    print()

def q34_four_digit_extraction():
    number = 9365
    ones = number % 10
    tens = (number // 10) % 10
    hundreds = (number // 100) % 10
    thousands = (number // 1000) % 10
    print("Q34 — Four-Digit Extraction (number = 9365):")
    print("Thousands Digit:", thousands)
    print("Hundreds Digit:", hundreds)
    print("Tens Digit:", tens)
    print("Ones Digit:", ones)
    print()

def q35_build_number():
    hundreds = 5
    tens = 8
    ones = 3
    number = hundreds * 100 + tens * 10 + ones
    print("Q35 — Build a Number from digits (hundreds=5,tens=8,ones=3):")
    print("Number:", number)
    print()

# Run all
if __name__ == "__main__":
    q21_ones_digit()
    q22_tens_digit()
    q23_hundreds_digit()
    q24_three_digit_analyzer()
    q25_four_digit_number()
    q26_sum_of_digits()
    q27_four_digit_sum()
    q28_product_of_digits()
    q29_reverse_three_digit()
    q30_reverse_four_digit()
    q31_place_value()
    q32_difference_first_last()
    q33_debug_digit_extraction()
    q34_four_digit_extraction()
    q35_build_number()