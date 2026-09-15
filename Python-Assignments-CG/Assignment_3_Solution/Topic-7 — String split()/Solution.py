# string_split_answers.py
# Q33 - Q41 (String split())

def q33_basic_split():
    text = "Python is easy"
    print("Q33 — Basic split():")
    print(text.split())  # ['Python', 'is', 'easy']
    print("Explanation: split() by default uses SPACE as separator.")
    print()


def q34_custom_separator():
    data = "apple,banana,mango"
    print("Q34 — Custom Separator:")
    print(data.split(","))  # ['apple', 'banana', 'mango']
    print()


def q35_separator_not_present():
    text = "Python is easy"
    print("Q35 — Separator Not Present:")
    print(text.split(","))  # ['Python is easy']
    print("Explanation: ',' not found, so no split happens.")
    print()


def q36_split_full_name():
    print("Q36 — Split Full Name:")
    name = "Rahul Kumar Sharma"
    parts = name.split()
    
    for part in parts:
        print(part)
    print()


def q37_multiple_inputs():
    print("Q37 — Multiple Inputs Using split():")
    full_name = "Rahul Kumar"  # demo input
    
    first_name, last_name = full_name.split()
    
    print("First Name:", first_name)
    print("Last Name:", last_name)
    print()


def q38_three_numbers():
    print("Q38 — Three Numeric Inputs:")
    nums = "10 20 30"  # demo input
    
    a, b, c = nums.split()
    total = int(a) + int(b) + int(c)
    
    print("Sum:", total)
    print()


def q39_student_record():
    print("Q39 — Student Record:")
    data = "Rahul,20,BTech,Ahmedabad"
    
    name, age, course, city = data.split(",")
    
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)
    print("City:", city)
    print()


def q40_email_analyzer():
    print("Q40 — Email Analyzer:")
    email = "rahul.kumar@gmail.com"
    
    username, domain = email.split("@")
    
    print("Username:", username)
    print("Domain:", domain)
    print()


def q41_sentence_analyzer():
    print("Q41 — Sentence Analyzer:")
    sentence = "Python is very powerful"
    
    words = sentence.split()
    
    print("First word:", words[0])
    print("Last word:", words[-1])
    print("Total words:", len(words))
    print()


if __name__ == "__main__":
    q33_basic_split()
    q34_custom_separator()
    q35_separator_not_present()
    q36_split_full_name()
    q37_multiple_inputs()
    q38_three_numbers()
    q39_student_record()
    q40_email_analyzer()
    q41_sentence_analyzer()


'''Q33:
['Python', 'is', 'easy']

Q34:
['apple', 'banana', 'mango']

Q35:
['Python is easy']

Q36:
Rahul
Kumar
Sharma

Q37:
First Name: Rahul
Last Name: Kumar

Q38:
Sum: 60

Q39:
Name: Rahul
Age: 20
Course: BTech
City: Ahmedabad

Q40:
Username: rahul.kumar
Domain: gmail.com

Q41:
First word: Python
Last word: powerful
Total words: 4'''