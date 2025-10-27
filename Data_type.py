# -------------------------STRING TYPE ---------------

# a = "My name is "
# b = "UZAIR"
# print (a+b) 



# --------------------INT TYPE-----------------

# a = 10
# b = 20
# c = a+ b
# print("The answer is :", c)



# -------------------- TYPE CASTING----------------------


########### converting string to int and then add 5 to it.  ###########


# x = "25"    # direct x = int("25") kar k bhi int type mein convert krskte hain
# y = int(x)
# z = 5 

# add = y + z

# print(add)
# print(type(add))


############ converting int to string and then concatenate it the "APPLE".  ###########


# y = 10
# x = str(y)
# z = "apple"

# concatenate = x + z

# print(concatenate)
# print(type(concatenate))



############ convert float to int ###########


# z = 4.7
# y = int(z) # convert krte hue float se int mein value int-floor ki taraf ati (na k ceiling ki)

# print(y)
# print(type(y))



############  a = True ko integer mein convert karo aur print karo. ###########


# a = True
# # print(a)
# # print(type(a))

# b = int(a) # true integer mein convert hone per is ki value 1 hoti hai

# print(b)
# print(type(b))



############ Ek variable num = 0 hai. integer se boolean mein convert karo — kya output aayega? ###########


# num = -8.89
# convert_to_boolean = bool(num)
# print(convert_to_boolean)
# print(type(convert_to_boolean))


############  try to convert interger/string to int  (and try with help of try and except )  ###########

# string_num = "100abc"
# num = int(string_num)
# print(string_num)
# print(type(string_num))
# print(num)
# print(type(num))

# # try:
# #     converted_num = int(string_num)
# #     print("converted number : ", converted_num)

# # except ValueError:
# #     print("Conversion failed")


#########------------- After creating new branch ----------------##############


####### String Functions ###########

# name = "Uzair Ahmed"
# print("upper function",name.upper())
# print("lower function",name.lower())
# print("replace function",name.replace("Uzair","uzair"))
# print("title function",name.title())
# print("capitalize function",name.capitalize())
# print("find function",name.find("Ahmed"))


### let's solve : WAP to check if a number entered by the user is odd or even.

# num = int(input("Enter a number: "))

# if (num % 2 == 0): 
#     print("The number is even.")
# else:
#     print("The number is odd.")



###

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))  
# num3 = int(input("Enter third number: "))

# if (num1 > num2) and (num1 > num3):
#     print("The largest number is first number which is:", num1)
# elif (num2 > num1) and (num2 > num3): 
#     print("The largest number is second number which is:", num2)
# else:
#     print("The largest number is third number which is:", num3);




#####   Q1. User se ek number input lo. Agar number positive hai to print karo "Positive number",agar negative hai to "Negative number",warna "Zero" print karo.  #####

# ask_input = int(input("Enter a number: "))
# if (ask_input > 0 ):
#     print("this is a positive number !!!")
# elif (ask_input < 0 ):
#     print("this is a negative number !!!")
# else:
#     print("It's a zero !!!")



##### Q2. User se ek letter input lo. Check karo kya wo vowel (a, e, i, o, u) hai ya consonant. Print result accordingly.  ####


# ask_input = input("Enter a vowel character: ")

# if  (ask_input == "a") or (ask_input == "A"):
#     print("its a vowel !!!")
# elif  (ask_input == "e") or (ask_input == "E"):
#     print("its a vowel !!!")
# elif  (ask_input == "i") or (ask_input == "I"):
#     print("its a vowel !!!")
# elif  (ask_input == "o") or (ask_input == "O"):
#     print("its a vowel !!!")
# elif  (ask_input == "u") or (ask_input == "U"):
#     print("its a vowel !!!")
# else:
#     print("It's a consonant !!!")

## !---CHATGPT LOGIC 

        # ask_input = input("Enter a character: ")

        # if ask_input.lower() in ['a', 'e', 'i', 'o', 'u']:
        #     print("It's a vowel !!!")
        # else:
        #     print("It's a consonant !!!")



###########  NESTED CONDITIONAL STATEMENT ############

### Q1. Age and Nationality Check
#### User se age aur nationality input lo.
#### Agar age >= 18 hai,
#### to check karo agar nationality == "Pakistani" hai,
#### to print "Eligible to vote".
#### Warna "Not eligible (different nationality)".
###Agar age < 18 hai to print "Not eligible (underage)".


 ###--- program for above case


# user_age = int(input("Enter your age: "))
# user_nationality = str.capitalize(input("Enter your nationality: "))

# if user_age >= 18 :
#     if user_nationality == "Pakistani":
#         print("Eligible to vote")
#     else:
#         print("Not eligible (different nationality)")
# else:
#     print("Not eligible (underage)")


### -----------------------------------------------########



### Q2. Login System

### User se username aur password input lo.
### Agar username "Uzair" hai,
### to check karo agar password "python123" hai,
### to print "Login successful".
### Warna "Wrong password".
### Agar username galat hai to print "Invalid username".

 ###--- program for above case

user_name = input("Enter your username: ")
password = input("Enter your password: ")

if user_name.lower() == "uzair": ### user_name input le k "if" k ander .lower k check krwaya
    if password == "python123":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Invalid username")
