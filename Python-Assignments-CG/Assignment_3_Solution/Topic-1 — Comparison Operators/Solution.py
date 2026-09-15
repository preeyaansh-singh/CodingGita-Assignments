# comparison_answers.py
# Q1 - Q4: Comparison operators — predictions shown as actual outputs

def q1_predict_output():
    a = 15
    b = 20
    print("Q1 — Predict the Output (a=15, b=20):")
    print(a < b)
    print(a > b)
    print(a == b)
    print(a != b)
    print(a <= b)
    print(a >= b)
    print()

def q2_compare_expressions():
    x = 10
    y = 10
    print("Q2 — Compare Expressions (x=10, y=10):")
    print(x == y)
    print(x != y)
    print(x < y)
    print(x <= y)
    print(x >= y)
    print()

def q3_comparison_with_arithmetic():
    a = 10
    b = 5
    print("Q3 — Comparison with Arithmetic (a=10, b=5):")
    print(a + b == 15)   # True
    print(a * b > 40)    # True (50 > 40)
    print(a - b != 5)    # False (10-5 == 5, so != 5 is False)
    print(a // b == 2)   # True (integer division)
    print()

def q4_string_comparison():
    print("Q4 — String Comparison (case sensitive):")
    print("Python" == "Python")
    print("Python" == "python")
    print("Hello" != "hello")
    print("Note: string comparison is case-sensitive; 'Python' != 'python' because of case.")
    print()

if __name__ == "__main__":
    q1_predict_output()
    q2_compare_expressions()
    q3_comparison_with_arithmetic()
    q4_string_comparison()

'''Q1 — Predict the Output (a=15, b=20):
True
False
False
True
True
False

Q2 — Compare Expressions (x=10, y=10):
True
False
False
True
True

Q3 — Comparison with Arithmetic (a=10, b=5):
True
True
False
True

Q4 — String Comparison (case sensitive):
True
False
True
Note: string comparison is case-sensitive; 'Python' != 'python' because of case.'''