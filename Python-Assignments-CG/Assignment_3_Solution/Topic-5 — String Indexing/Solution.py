# string_indexing_answers.py
# Q19 - Q23 (String Indexing)

def q19_basic_indexing():
    text = "PYTHON"
    print("Q19 — Basic Indexing (text = 'PYTHON'):")
    print("First character      ->", text[0])
    print("Second character     ->", text[1])
    print("Last character       ->", text[-1])
    print("Second-last character->", text[-2])
    print()


def q20_positive_negative_indexing():
    text = "COMPUTER"
    print("Q20 — Positive and Negative Indexing (text = 'COMPUTER'):")
    
    print("text[0]  ->", text[0])   # C
    print("text[3]  ->", text[3])   # P
    print("text[-1] ->", text[-1])  # R
    print("text[-3] ->", text[-3])  # T
    print()


def q21_predict_output():
    text = "PYTHON"
    print("Q21 — Predict the Output:")
    print(text[0])   # P
    print(text[2])   # T
    print(text[-1])  # N
    print(text[-2])  # O
    print()


def q22_user_input_demo():
    print("Q22 — Indexing User Input (demo test cases):")
    
    test_words = ["Python", "Computer", "Hello"]
    
    for word in test_words:
        print(f"Word: {word} -> First: {word[0]}, Last: {word[-1]}")
    
    # Uncomment for real input
    # user_word = input("Enter a word: ")
    # print("First:", user_word[0])
    # print("Last:", user_word[-1])
    
    print()


def q23_think_indexing():
    word = "PROGRAM"
    print("Q23 — Think Carefully About Indexing (word = 'PROGRAM'):")
    
    print("word[0]  ->", word[0])   # P
    print("word[2]  ->", word[2])   # O
    print("word[-1] ->", word[-1])  # M
    print("word[-4] ->", word[-4])  # G
    print()


if __name__ == "__main__":
    q19_basic_indexing()
    q20_positive_negative_indexing()
    q21_predict_output()
    q22_user_input_demo()
    q23_think_indexing()


'''Q19:
P Y N O

Q20:
C P R T

Q21:
P
T
N
O

Q22:
Python -> P n
Computer -> C r
Hello -> H o

Q23:
P O M G'''