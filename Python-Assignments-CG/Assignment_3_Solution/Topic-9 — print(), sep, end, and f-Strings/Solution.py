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

# ---------------- MAIN ---------------- #

if __name__ == "__main__":
    q49_sep()
    q50_end()
    q51_sep_and_end()
    q52_student_intro()
    q53_formatted_price()
