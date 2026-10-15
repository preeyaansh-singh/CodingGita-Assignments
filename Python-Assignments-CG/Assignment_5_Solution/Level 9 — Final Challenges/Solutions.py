# Q68. Number Profile
num=int(input())
digits=0
total=0
largest=0
smallest=9
even=0
odd=0
for i in range(num):
    if num==0:
        break
    digit=num%10
    digits+=1
    total+=digit
    if digit>largest:
        largest=digit
    if digit<smallest:
        smallest=digit
    if digit%2==0:
        even+=1
    else:
        odd+=1
    num//=10
print("Digits:",digits)
print("Sum:",total)
print("Largest:",largest)
print("Smallest:",smallest)
print("Even Digits:",even)
print("Odd Digits:",odd)

# Q69. String Balance Challenge
s=input()
total=0
vowels=0
consonants=0
uppercase=0
lowercase=0
even_index=0
for i,ch in enumerate(s):
    total+=1
    if i%2==0:
        even_index+=1
    if ch!=" ":
        if ch.lower() in "aeiou":
            vowels+=1
        else:
            consonants+=1
        if "A"<=ch<="Z":
            uppercase+=1
        elif "a"<=ch<="z":
            lowercase+=1
print("Total Characters:",total)
print("Vowels:",vowels)
print("Consonants:",consonants)
print("Uppercase:",uppercase)
print("Lowercase:",lowercase)
print("Even Index Characters:",even_index)