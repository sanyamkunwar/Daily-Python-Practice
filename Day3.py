# ---------------------------------------------------------------
# python best courses https://courses.tanpham.org/
# ---------------------------------------------------------------
# Challenge
# Given a string, find the length of the longest substring
# without repeating characters.

# Examples:
# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3.
# ---------------------------------------------------------------
# Algorithm

# In summary : Form all posible sub_strings from original string, then return length of longest sub_string

# - start from 1st character, form as long as posible sub string

#             - Add first character to sub string
#             - Add second character to sub string if second character not exist in sub string
#             ...
#             - Repeate until got a character which already exist inside sub string or 
    
    
# - start from 2nd character, form as long as posible sub string

#             - Add first character to sub string
#             - Add second character to sub string if second character not exist in sub string
#             ...
#             - Repeate until got a character which already exist inside sub string


# ....


# - start from final character, form as long as posible sub string
#             - Add first character to sub string
#             - Add second character to sub string if second character not exist in sub string
#             ...
#             - Repeate until got a character which already exist inside sub string
# ---------------------------------------------------------------

str = "abcbb"

def longest_non_repeat(str):
    
    # init start position and max length     
    i=0
    max_length = 1

    for i,c in enumerate(str):

        # init counter and sub string value         
        start_at = i
        sub_str=[]

        # continue increase sub string if did not repeat character         
        while (start_at < len(str)) and (str[start_at] not in sub_str):
            sub_str.append(str[start_at])
            start_at = start_at + 1

        # update the max length   
        if len(sub_str) > max_length:
            max_length = len(sub_str)

        print(sub_str)
        
    return max_length

print(longest_non_repeat(str))
#================================================================================================

items = [
    ("item1", 12.20),
    ("item2", 15.10),
    ("item3", 24.5)
]

# lambda function to sort items by price
filtered = filter(lambda item: item[1] >= 15, items)
print(list(filtered))

#================================================================================================
# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5 
# Expected Result : 615

a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)

#================================================================================================

# Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
# Sample input : 5
# Sample output : The number is odd.
num = int(input("Input an integer : "))
print("The number is even." if num%2 == 0 else "The number is odd.")
#================================================================================================

# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = input("What is your name: ")
age = int(input("How old are you: "))
year = str((2024 - age)+100)
print(name + " will be 100 years old in the year " + year)

#================================================================================================