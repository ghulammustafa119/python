# functions----
# simple function
def greet():
    print("Hello Ghulam Mustafa Bhutto")
# greet()
#--------------------------------------
# function with parameter
def greet(name):
    print(f"Hello {name}")
# greet("Ghulam Mustafa Bhutto")
# greet("Ghulam Mujtaba Bhutto")
# greet("Nayab Mustafa Bhutto")
#---------------------------------------------
# Key Difference
#         Environment	           Needs print()?	                         Why?
# Google Colab / Jupyter Notebook	 ❌ No	  Automatically shows the last expression's result.
# VS Code / Standard Python Script	 ✅ Yes	  Doesn't automatically display return values.
# Conclusion
# If you run your code in VS Code without print(), Python executes it but doesn’t display anything. In Colab, it displays the last returned value automatically

def add_two(a, b):
    return a + b
# print(add_two(15, 10))
#----------------------------------------------------------------------------------
# function with default parameter
def greet_with_default(name = "Mustafa"):
    print(f"Hello {name}")
# greet_with_default("Mujtab")
# greet_with_default("Nayab")

def add_two(a = 10, b = 20):
    return a + b
# print(add_two(15, 10))
# print(add_two())
#------------------------------------------------------------------------------
# calculator
# def calculator(a, b, operation):
#     if(operation == "add"):
#         return a + b
#     elif(operation == "subtract"):
#         return a - b
#     elif(operation == "multiply"):
#         return a * b
#     elif(operation == "divide"):
#         return a / b
#     else:
#         return "invalid operation"
# print(calculator(5, 10, "add"))           # Output: 15
# print(calculator(5, 10, "subtract"))      # Output: 5
# print(calculator(5, 10, "multiply"))      # Output: 50
# print(calculator(10, 5, "divide"))        # Output: 2.0
#---------------------------------------------------
def calculator(a, b, operation):
    operation = operation.lower()  # Convert to lowercase for flexible input
    
    if (operation == "add"):
        return a + b
    elif (operation == "subtract"):
        return a - b
    elif (operation == "multiply"):
        return a * b
    elif (operation == "divide"):
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b
    else:
        return "Invalid operation"

# print(calculator(5, 10, "add"))       # Output: 15
# print(calculator(5, 10, "subtract"))  # Output: -5
# print(calculator(5, 10, "Multiply"))  # Output: 50
# print(calculator(10, 5, "divide"))    # Output: 2.0
# print(calculator(12, 0, "divide"))    # Handles division by zero
# print(calculator(5, 10, "MOD"))       # Handles invalid operation
#----------------------------------------------------------------------
# making a cup of tea
def make_tea():
    "Boiling water..."
    "Adding tea leaves..."
    "Pouring milk..."
    "Adding sugar..."
    return "Tea is ready! ☕"
tea1 = make_tea()
# print(f"{tea1} for me")
tea2 = make_tea()
# print(f"{tea2} and me")
tea3 = make_tea()
# print(f"{tea3} and and me")
tea4 = make_tea()
# print(f"{tea4} ok.... for me")
#------------------------------------------
def cal_llm(Prompt):             # llm means: (large language model)
  print(f"user: {Prompt}")
  name = "Ghulam Mustafa Bhutto"           
  return f"Ai: Hello, {name} How can I assist you today? 😊"
response = cal_llm("Hello! My name is Ghulam Mustafa Bhutto")
print(response)