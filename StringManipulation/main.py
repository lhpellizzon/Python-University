
# Length
# -------------------->
# We can make mathematical operations on string + length
# test_string = "string here"
# string_length = len(test_string)
# print(string_length)

# Concatenation
# -------------------->
# We cannot concat string and numbers, but we can multiply
# how many times we want to concat the string
# test_string = "string here" * 5
# test_string = "string here" + 5 cannot operate
# print(test_string)

# Index (start at 0)
# -------------------->
# string = "string"
# string_index_value = string[index number here]
# print(string_index_value)

# Slice
# -------------------->
# string = "string here"
# string_slice_value = string[start :  one past where we want to finish]
# print(string_slice_value)

# Find   will search and find the index of the first letter passed as an argument
# -------------------->
# string = "hello"
# indexFound = string.find('l')
# print(indexFound)

# Remove Chars strip(chars ? chars : null)
# -------------------->
# strip() => remove from both sides
# rstrip() => right side
# lstrip() => left side
# string = "  string  "
# stripped_string = string.strip()
# print(stripped_string)

# Replace Chars replace(to be replaced, char )
# -------------------->
# string = "replace me"
# stripped_string = string.replace("replace", "fodase")
# print(stripped_string)


# Exercise 1
# -------------------->
# Turn this string into a string "mouse" without typing mouse
# string = 'A famous Irish Mathematician is Robert Boole'
# index_m = string.find("m")
# # first_part = string[index_m: index_m + 4]
# index_e = string.find("e")
# result = string[index_m: index_m + 4] + string[index_e]
# print(result)


# Exercise 2 prompt user for a string > 5
# -------------------->
# def user_input():
#     user_input_value = input("Please, enter a message equal or longer than 5 characters\n")
#     user_input.strip()
#     if len(user_input_value) < 5:
#         print("Please, make sure you entered a message equal or longer to 5 characters")
#         return user_input()
#     else:
#         first_part = user_input_value[0:3]
#         second_part = user_input_value[len(user_input_value) - 2: len(user_input_value)]
#         result = first_part + second_part
#         print(result)
#
#
# user_input()


# Exercise 3 put € in every start of input
# -------------------->
# def put_symbol():
#     user_input_value = input("Enter a message\n")
#
#     if user_input_value == "":
#         print("Please, make sure you enter a message")
#         return put_symbol()
#
#     result = user_input_value.replace(user_input_value[0], "€")
#
#     print(f"First character {user_input_value[0]} changed to {result}")
#
# put_symbol()


# Exercise 4 take two inputs and swap the first char at both and output one string
# -------------------->
# def user_input():
#     first_string = input("Enter first string\n")
#     second_string = input("Enter second string\n")
#
#     first_string_changed = first_string.replace(first_string[0], second_string[0])
#     second_string_changed = second_string.replace(second_string[0], first_string[0])
#
#     result = first_string_changed + " " + second_string_changed
#
#     print(result)
#
# user_input()


# Exercise 5 replace all instances with "€"
# -------------------->
# def user_input():
#     user_value = input("Enter first string\n")
#     result = user_value.replace(user_value[0], "€")
#
#     print(result)
#
# user_input()


# Exercise 6 replace second char in a string
# -------------------->
# def user_input():
#     user_value = input("Enter first string\n")
#     result = user_value.replace(user_value[1], "")
#
#     print(result)
#
# user_input()



