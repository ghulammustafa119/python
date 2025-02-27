message = "would you like to learn some python with me"  #string
name = "Ghulam Mustafa Bhutto"  # string
# print(f"""Hello! {name} {message}""") # using (string) and (f string) and (doc string)

# print(f"my name is {name}") # use of (f string)
#---------------------------------------------------------------
paragraph = """Hello        
Ghulam Mustafa Bhutto 
would you like to learn some python with me"""    # doc string
# print(paragraph)

# print(f"Hello {name} {message} ")
#-------------------------------------------------------------
first_name = "Ghulam Mujtaba Bhutto"
# print(
#     f"""
# Hi {first_name},
# you got a free coupon code: Happy New Year 2025
# Best Regards,
# Ghulam Mustafa Bhutto

# """
# )
#----------------------------------------------------------------
example =     f"""
Hi {first_name},
you got a free coupon code: Happy New Year 2025
Best Regards,
Ghulam Mustafa Bhutto

"""
# print(example)
#------------------------------------------------------------
# opprators

num1 = 10
num2 = 20
res = num1 + num2
# print(res)

num1 = 10
num2 = 20
res = num1 - num2
# print(res)

num1 = 10
num2 = 20
res = num1 * num2
# print(res)

num1 = 10
num2 = 20
res = num1 / num2
# print(res)

num1 = 20
num2 = 2
res = num1 % num2
# print(res)

num1 = 10
num2 = 3
res = num1 ** num2
# print(res)
#--------------------------------
#  Making rabri
faculty = 12
admin = 4
students = 100
absent = 15
per_person_rabri = 250
total_members = faculty + admin + students 
total_present_members = total_members - absent

print(f"total present members : {total_present_members}")
total_rabri_gram = total_present_members * per_person_rabri


print(f"total rabri in grams : {total_rabri_gram}g")
print(f"total rabri in kilo grams : {total_rabri_gram // 1000}kg") # (if you want answer in kg not in grams then apply divide sign two times (total_rabri_gram // 1000)) then answer will be 25kg
