import os
import random


os.system("clear")
print("MADLIBS\n")

f = open("public/frases.txt", "r")
lines = f.readlines()
randomLine = random.randint(0, len(lines)-1)
frase = lines[randomLine].strip()

solution = ""

i = 0
j = 0
while i < len(frase):
    word = ""
    if frase[i] == "_":
        while frase[i] != "(":
            i += 1
        i += 1
        while frase[i] != ")":
            word += frase[i]
            i += 1
        i += 1
        word = input("Introduce a " + word + ": ")
        solution += word
        j += 1
    
    solution += frase[i]
    i += 1
    
os.system("clear")
print("MADLIBS\n")
print(solution)