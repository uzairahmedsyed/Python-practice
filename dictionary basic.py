

first_dict = {
    "name" : "abc",
    "age" : 20,
    "city" : "karachi",
    "cities" : {
        "first_city": "lahore",
        "second_city":"islamabad"
    }
}

# print(f"full dictionary: {first_dict}")
# print(f"name of main dictionary: {first_dict["name"]}")
# print(f"age of main dictionary: {first_dict["age"]}")
# print(f"cities of main dictionary: {first_dict["cities"]}")
# print(f"first city of sub dictionary: {first_dict["cities"]["first_city"]}")

# print(f"full dictionary: {len(first_dict)}")
# print(f"name of main dictionary: {first_dict["name"]}")
# print(f"age of main dictionary: {first_dict["age"]}")
# print(f"cities of main dictionary: {first_dict["cities"]}")
# print(f"first city of sub dictionary: {first_dict["cities"]["first_city"]}")

####========================================================####


#### dictionary mein user se input le k KEY:VALUE save krwana


# grocery = {}

# user_item = input("Enter any grocery item: ")
# user_price = float(input("Enter the price of the item: "))

# grocery.update({user_item:user_price})
# print(grocery[user_item])




####========================================================================================##############



# Ek program likho jo 3 students ke names aur marks input le kar ek dictionary banaye.
# Phir user se pooche kis student ka result dekhna hai, aur uska marks print kare.
# (Agar naam nahi mile to message de "Student not found")


# std = {}

# firstStd = input("Enter first student name: ")
# firstStdMarks = int(input("Enter first student marks: "))

# secondStd = input("Enter second student name: ")
# secondStdMarks = int(input("Enter second student marks: "))

# thirdStd = input("Enter third student name: ")
# thirdStdMarks = int(input("Enter third student marks: "))

# std.update({firstStd:firstStdMarks, secondStd:secondStdMarks, thirdStd:thirdStdMarks})

# print(std)

# userName = input("Enter the student name of which you want their marks: ")

# ##### smart way to use if-else 

# ### dircetly user input se dictionary mein check krwaya k mujood hai
# if (userName in std):
#     print(f"{userName} got std[userName] marks ")
# else:
#     print("Not found!")

# ### ek ek kar k match krwaya jo k best practice nahi hoti (upar wala sahi hai)
# # if (userName == firstStd):
# #     print(std[firstStd])
# # elif(userName == secondStd):
# #     print(std[secondStd])
# # elif(userName == thirdStd):
# #     print(std[thirdStd])
# # else:
# #     print("Not found!")




# Ek dictionary banao jisme fruits aur unki prices hon (example: {"apple": 100, "banana": 50, "mango": 150})
# Phir user se ek fruit ka naam aur quantity input lo.
# Total price calculate karo aur agar fruit dictionary mein nahi hai to message do “Not available”.



fruits = {"apple": 100, "banana": 50, "mango": 150}

fruitsInput = input("Enter the fruit name: ")
fruitsQuantity = int(input("Enter the quantity of fruit: "))

### fruit name check krwaya FRUITS dictionary mein
if fruitsInput in fruits:
    ### user quantity ko mutliple krwaya us fruit k price se jo user se fruit name inpu dia tha
    totalPrice = fruitsQuantity * fruits[fruitsInput]
    print(totalPrice)
else:
    print("Not found!")