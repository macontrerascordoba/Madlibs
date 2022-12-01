import os
import random


os.system("clear")
print("MADLIBS\n")

f = open("public/sentences.txt", "r")
lines = f.readlines()
randomLine = random.randint(0, len(lines)-1)
sentence = lines[randomLine].strip()

solution = ""

i = 0
j = 0
while i < len(sentence):
    word = ""
    if sentence[i] == "_":
        while sentence[i] != "(":
            i += 1
        i += 1
        while sentence[i] != ")":
            word += sentence[i]
            i += 1
        i += 1
        word = input("Introduce a " + word + ": ")
        solution += word
        j += 1
    
    solution += sentence[i]
    i += 1
    
os.system("clear")
print("MADLIBS\n")
print(solution)

input("\nPress Enter to exit...")
os.system("clear")