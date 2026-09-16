# print_and_debugging_answers.py
# Q49 - Q59 (with expected outputs)

def q49_sep():
    print("Q49 — sep:")
    print("2026", "09", "09", sep="-")
    print("Expected Output: 2026-09-09\n")


def q50_end():
    print("Q50 — end:")
    print("Hello", end=" ")
    print("Python")
    print("Expected Output: Hello Python\n")


def q51_sep_and_end():
    print("Q51 — sep and end:")
    print(10, 20, 30, sep="-")
    print(40, 50, 60, sep="-")
    print("Expected Output:\n10-20-30\n40-50-60\n")


def q52_student_intro():
    print("Q52 — Student Introduction:")
    name = "Rahul"
    age = 20
    city = "Ahmedabad"
    course = "B.Tech"

    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    print(f"Course: {course}")

    print("Expected Output:")
    print("Name: Rahul")
    print("Age: 20")
    print("City: Ahmedabad")
    print("Course: B.Tech\n")


def q53_formatted_price():
    print("Q53 — Formatted Price:")
    price = 120.678
    print(f"{price:.2f}")
    print("Expected Output: 120.68\n")


# ---------------- DEBUGGING ---------------- #

def q54_string_integer():
    print("Q54 — String and Integer Fix:")
    age = int(input("Enter age: "))
    result = age + 5
    print("Age after 5 years:", result)
    print("Expected Output: (depends on input)\n")


def q55_quotes():
    print("Q55 — Incorrect Quotes Fix:")
    print("It's Python")
    print("Expected Output: It's Python\n")


def q56_slicing_fix():
    print("Q56 — Slicing Fix:")
    text = "Python"
    print(text[1:4])
    print("Expected Output: yth\n")


def q57_split_fix():
    print("Q57 — Split Fix:")
    a, b = input("Enter two numbers: ").split()
    print(a, b)
    print("Expected Output: depends on input\n")


def q58_string_vs_numeric():
    print("Q58 — String vs Numeric Addition:")
    a, b = input("Enter two numbers: ").split()
    print("String Addition:", a + b)
    print("Numeric Addition:", int(a) + int(b))
    print("Expected Output Example:\nString Addition: 1020\nNumeric Addition: 30\n")


def q59_escape_fix():
    print("Q59 — Escape Sequence Fix:")
    print("C:\\new\\test")
    print("Expected Output: C:\\new\\test\n")


# ---------------- MAIN ---------------- #

if __name__ == "__main__":
    q49_sep()
    q50_end()
    q51_sep_and_end()
    q52_student_intro()
    q53_formatted_price()

    # Uncomment if you want to test input-based ones
    # q54_string_integer()
    q55_quotes()
    q56_slicing_fix()
    # q57_split_fix()
    # q58_string_vs_numeric()
    q59_escape_fix()