# Q37. Print Characters with Index
s=input()
index=0
for ch in s:
    print(index,ch)
    index+=1

# Q38. Count Characters Without len()
s=input()
count=0
for ch in s:
    count+=1
print(count)

# Q39. Count Vowels and Consonants
s=input()
vowels=0
consonants=0
for ch in s:
    if ch!=" ":
        if ch.lower() in "aeiou":
            vowels+=1
        else:
            consonants+=1
print(f"Vowels = {vowels}, Consonants = {consonants}")

# Q40. Character Frequency
s=input()
target=input()
count=0
for ch in s:
    if ch==target:
        count+=1
print(count)

# Q41. First Occurrence Position
s=input()
target=input()
position=-1
index=0
for ch in s:
    if ch==target:
        position=index
        break
    index+=1
if position==-1:
    print("Not Found")
else:
    print(position)

# Q42. Count Uppercase and Lowercase
s=input()
uppercase=0
lowercase=0
for ch in s:
    if "A"<=ch<="Z":
        uppercase+=1
    elif "a"<=ch<="z":
        lowercase+=1
print(f"Uppercase = {uppercase}, Lowercase = {lowercase}")

# Q43