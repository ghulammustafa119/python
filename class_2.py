#  if else

# person_age = 15

# if (person_age > 18):
#     print("you are allowed")
# else:
#     print("you are not allowed")
#---------------------------------------------
# Input example

# name = input("what is your name?")
# print(f"Hello,{name} !")

# name = input("what is your name?")
# age = input("How old are you?")
# print(f"Hello, {name}! yor are {age} years old.")
#--------------------------------------------------------------
# comparison operators....
# age = int(input("Enter your age:"))
# if(age < 18):
#   print("you are a minor.")
# elif(age == 18):
#   print("you are a young person.")
# elif(age == 80):
#   print("you are old man!.")
# else:
#   print("you are an adulit.")
#---------------------------------------------------
# score = int(input("Enter your score: "))
  
# if (score >= 90 and score <= 100):
#     grade = "A"
#     print(f"According to your score, your grade is: {grade}.")
# elif (score >= 80 and score <= 89):
#     grade = "B"
#     print(f"According to your score, your grade is: {grade}.")
# elif (score >= 70 and score <= 79):
#     grade = "C"
#     print(f"According to your score, your grade is: {grade}.")
# elif (score >= 60 and score <= 69):
#     grade = "D"
#     print(f"According to your score, your grade is: {grade}.")
# elif (score >=33 and score <= 59):
#     grade = "E"
#     print(f"According to your score, your grade is: {grade}.")
# else:
#     print("You are fail.")
#-------------------------------------------------------------

# is_hungry = True
# burger_lover = True
# pizza_lover = False
# if(is_hungry and (burger_lover or pizza_lover)):
#   print("let's order the food")
#-------------------------------------------------
# is_hungry = False
# burger_lover = False
# pizza_lover = False
# if(is_hungry and (burger_lover or pizza_lover)):
#   print("let's order the food")
# elif(is_hungry):
#   print("let's go to sleep.")
#-------------------------------------------------------------   
# is_hungry = True
# burger_lover = False
# pizza_lover = False
# if(is_hungry and (burger_lover or pizza_lover)):
#   print("let's order the food")
# elif(is_hungry):
#   print("let's go to sleep.")
#---------------------------------------------
# is_hungry = True
# burger_lover = False
# pizza_lover = True
# if(is_hungry and (burger_lover or pizza_lover)):
#   print("let's order the food")
# elif(is_hungry):
#   print("let's go to sleep.")
#----------------------------------------------------  
# is_hungry = False
# burger_lover = False
# pizza_lover = True
# if(is_hungry and (burger_lover or pizza_lover)):
#   print("let's order the food")
# elif(is_hungry):
#   print("let's go to sleep.")
# else:
#   print("Not hungry.")
#--------------------------------------------------
is_hungry = False
burger_lover = True
pizza_lover = True
          #  False            or   True (output will true)
if(is_hungry and burger_lover or pizza_lover):
  print("let's order the food")
elif(is_hungry):
  print("let's go to sleep.")
else:
  print("Not hungry.")

