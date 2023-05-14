# -*- coding: utf-8 -*-
"""
Created on Mon May 15 03:05:12 2023

@author: jeyih
"""

import json
import random
import os

specialty = {}
specialty[1]="心臟科"
specialty[2]="胸腔科"
specialty[3]="消化科"
specialty[4]="腎臟科"
specialty[5]="模擬考"
specialty[6]="感染科"
specialty[7]="內分泌新陳代謝科"
specialty[8]="風濕免疫科"
specialty[9]="血液腫瘤科"
specialty[10]="神經科"
specialty[11]="精神科"
specialty[12]="皮膚科"

for i in range(1,13):
    print( str(i) + " " + specialty[i], end = "  ")
    if i % 3 == 0: print("")

print("*********************************************************")
s = input("Enter the ordinal number for the specialty you like : " )

for i in range(3):
    print("")

with open(f'qbank_{s}.json', 'r') as fp:
    data = json.load(fp)

print(f"There are {len(data)} questions in this specialty ! Good Luck ! ")
print("")
print("")
input("Enter to continue... ")
print("")
print("")

strike = 0 
while strike < 10:
    question, answer = random.choice(list(data.items()))
    print(question)
    for i in range(3):
        print("")
    ans = input("What is your answer ? ")
    ans = ans.upper()
    if ans != "" and ans in answer:
        print("Correct !")
        strike += 1
    else:
        print("You are wrong ! ")
        print("The correct answer is " + answer + ".")
        strike = 0
    print("")
    print("")
    input("Enter to continue")
    print("")
    print("")

print("You pass the exam!!")
