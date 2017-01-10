print("""
╔╗─╔╗────────╔═╗╔═╗─────╔╗──╔═══╗───╔╗──╔╗──────╔╗╔═╗───────────╔═╗╔═╗
║║─║║────────║║╚╝║║─────║║──╚╗╔╗║───║╚╗╔╝║──────║║║╔╝───────────║║╚╝║║
║╚═╝╠══╦╗╔╗╔╗║╔╗╔╗╠╗╔╦══╣╚═╗─║║║╠══╗╚╗╚╝╔╬══╦╗╔╗║╚╝╝╔═╗╔══╦╗╔╗╔╗║╔╗╔╗╠══╦╗╔╗
║╔═╗║╔╗║╚╝╚╝║║║║║║║║║║╔═╣╔╗║─║║║║╔╗║─╚╗╔╝║╔╗║║║║║╔╗║║╔╗╣╔╗║╚╝╚╝║║║║║║║╔╗╠╬╬╝
║║─║║╚╝╠╗╔╗╔╝║║║║║║╚╝║╚═╣║║║╔╝╚╝║╚╝║──║║─║╚╝║╚╝║║║║╚╣║║║╚╝╠╗╔╗╔╝║║║║║║╔╗╠╬╬╗
╚╝─╚╩══╝╚╝╚╝─╚╝╚╝╚╩══╩══╩╝╚╝╚═══╩══╝──╚╝─╚══╩══╝╚╝╚═╩╝╚╩══╝╚╝╚╝─╚╝╚╝╚╩╝╚╩╝╚╝

A 7 question quiz on Max""")
score = 0
#Q1
print("""
Question 1: How old am I?
""")
answer1 = float(input())
if answer1 == 17:
    score = score+1
else:
    score = score+0
    answer1 = "f"
#Q2
print("""
Question 2: What do I like to do in my free time?
a) Go Outside
b) Excersise
c) Play Videogames
d) Do My Schoolwork
""")
answer2 = input()
if answer2 == "c" or answer2 == "C":
    score = score+1
else:
    score = score+0
    answer2 = "f"
#Q3
print("""
Question 5: How many years have I been at SOF?
""")
answer3 = float(input())
if answer3 == 7:
    score = score+1
else:
    score = score+0
    answer3 = "f"
#Q4
print("""
Question 4: What kind of hair do I have?
a) Brown
b) Green
c) Purple
d) Curly
""")
answer4 = input()
if answer4 == "d" or answer4 == "D":
    score = score+1
else:
    score = score+0
    answer4 = "f"
#Q5
print("""
Question 5: Was question 3 question 3?
Please answer "yes" or "no".
""")
answer5 = input()
if answer5 == "no" or answer4 == "No" or answer4 == "nO" or answer4 == "NO":
    score = score+1
else:
    score = score+0
    answer5 = "f"
#Q6
print("""
Question 6: Which hand has my scar?
Answer "left" or "right"
""")
answer6 = input()
if answer6 == "right" or answer6 == "Right":
    score = score+1
else:
    score = score+0
    answer6 = "f"
#Q7
print("""
Question 7: How many plays have I been in?"
a) 1
b) 3
c) 5
""")
answer7 = input()
if answer7 == "b" or answer7 == "B":
    score = score+1
else:
    score = score+0
    answer7 = "f"
print("You got a score of ", score, " out of a possible 7.")
if score == 7:
      print("""You know me, buddy.
▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐
▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐█████████▐▐▐▐▐▐▐▐▐▐▐▐▐ 
▐▐▐▐▐▐▐▐▐▐▐▐▐█████████████████▐▐▐▐▐▐▐▐▐▐ 
▐▐▐▐▐▐▐▐▐▐███████▐▐▐▐▐▐█████████▐▐▐▐▐▐▐▐ 
▐▐▐▐▐▐▐▐▐█████▐▐▐▐▐▐▐▐▐▐▐▐▐▐█████▐▐▐▐▐▐▐ 
▐▐▐▐▐▐▐█████▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐████▐▐▐▐▐▐ 
▐▐▐▐▐▐████▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐███▐▐▐▐▐ 
▐▐▐▐▐████▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐███▐▐▐▐ 
▐▐▐▐████▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐███▐▐▐ 
▐▐▐▐███▐▐▐▐▐▐▐████▐▐▐▐▐▐▐▐██▐▐▐▐▐▐▐██▐▐▐ 
▐▐▐███▐▐▐▐▐▐▐▐████▐▐▐▐▐▐▐████▐▐▐▐▐▐███▐▐ 
▐▐▐███▐▐▐▐▐▐▐▐████▐▐▐▐▐▐▐████▐▐▐▐▐▐▐██▐▐ 
▐▐███▐▐▐▐▐▐▐▐▐▐██▐▐▐▐▐▐▐▐███▐▐▐▐▐▐▐▐███▐ 
▐▐███▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐███▐ 
▐▐███▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐███▐ 
▐▐███▐▐▐▐▐██▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐███▐ 
▐▐███▐▐▐▐▐██▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐███▐ 
▐▐███▐▐▐▐▐▐██▐▐▐▐▐▐▐▐▐▐▐▐▐▐██▐▐▐▐▐▐▐███▐ 
▐▐████▐▐▐▐▐▐███▐▐▐▐▐▐▐▐▐▐▐██▐▐▐▐▐▐▐▐███▐ 
▐▐▐███▐▐▐▐▐▐▐█████▐▐▐▐▐████▐▐▐▐▐▐▐▐███▐▐ 
▐▐▐▐███▐▐▐▐▐▐▐▐▐█████████▐▐▐▐▐▐▐▐▐▐███▐▐ 
▐▐▐▐█████▐▐▐▐▐▐▐▐██▐▐██▐▐█▐▐▐▐▐▐▐▐███▐▐▐ 
▐▐▐▐▐▐████▐▐▐▐▐▐▐██▐▐▐██▐██▐▐▐▐▐▐███▐▐▐▐ 
▐▐▐▐▐▐▐█████▐▐▐▐▐▐███▐▐▐▐██▐▐▐▐▐████▐▐▐▐ 
▐▐▐▐▐▐▐▐▐██████▐▐▐▐▐██████▐▐▐▐████▐▐▐▐▐▐ 
▐▐▐▐▐▐▐▐▐▐▐███████▐▐▐▐▐▐▐▐▐▐█████▐▐▐▐▐▐▐ 
▐▐▐▐▐▐▐▐▐▐▐▐▐██████████████████▐▐▐▐▐▐▐▐▐ 
▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐█████████▐▐▐▐▐▐▐▐▐▐▐▐▐
▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐
""")
elif score >5:
      print("You know me.")
elif score >3:
      print("You know.")
elif score >1:
      print("You.")
elif score == 0:
      print(".")
if answer1 == "f":
    print("Question 1's answer was 17. I am 17 years old.")
elif answer2 == "f":
    print("""Question 2's answer was "Play Videogames", or c. Duh I play videogames.""")
elif answer3 == "f":
    print("Question 3's answer was 7. I've been here since 6th grade.")
elif answer4 == "f":
    print("""Question 4's answer was "Curly", or d. My hair is curly, and brown, but the question is asking for my hair type ;^).""")
elif answer5 == "f":
    print("Question 5's answer was no. It goes Question 1, 2, 5, 4, 5.")
elif answer6 == "f":
    print("Question 6's answer was right. My right hand has a scar. 9th grade, I broke it.")
elif answer7 == "f":
    print("Question 7's answer was 3. Almost Maine, Addams Family, and Clyboune Park.")
