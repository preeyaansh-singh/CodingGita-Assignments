# assignment_ops_answers.py
# Q5 - Q6: Assignment operators — trace values and practice

def q5_trace_value():
    x = 20
    print("Q5 — Trace the Value (start x = 20)")
    print("Initial x:", x)

    x += 10
    print("After x += 10 ->", x)

    x -= 5
    print("After x -= 5  ->", x)

    x *= 2
    print("After x *= 2  ->", x)

    x //= 5
    print("After x //= 5 ->", x)

    print("Final x:", x)
    print()

def q6_assignment_practice():
    marks = 50
    print("Q6 — Assignment Operator Practice (start marks = 50)")
    print("Initial marks:", marks)

    marks += 10
    print("After marks += 10 ->", marks)

    marks -= 5
    print("After marks -= 5  ->", marks)

    marks *= 2
    print("After marks *= 2  ->", marks)

    print("Final marks:", marks)
    print()

if __name__ == "__main__":
    q5_trace_value()
    q6_assignment_practice()


'''Q5 — Trace the Value (start x = 20)
Initial x: 20
After x += 10 -> 30
After x -= 5  -> 25
After x *= 2  -> 50
After x //= 5 -> 10
Final x: 10

Q6 — Assignment Operator Practice (start marks = 50)
Initial marks: 50
After marks += 10 -> 60
After marks -= 5  -> 55
After marks *= 2  -> 110
Final marks: 110'''

'''Thank you'''