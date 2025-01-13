# Write a Python program to print the following string in a specific format (see the output). Go to the editor

# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" 

# Output :

# Twinkle, twinkle, little star,
# 	How I wonder what you are! 
# 		Up above the world so high,
# 		Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
# 	How I wonder what you are

# ----------------------------------------------------

# Hints
# Using \n (newline) and \t (tab) to format the string

# print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

# def mot(b):
#     a=[]
#     for i in range(len(b)-1):
#         while b[i] not in a:
#             a+=b[i]
#             i=i+1
#         else:
#             break
#     return a       

# print(mot("abcbb"))
# print(mot('hgdjuhg'))
import numpy as np
def mot(b):
    a=np.zeros(len(b))
    for j in range(0,len(b)-2):
        for i in range(len(b)-1):
            while b[i] not in a:
                a[i,:]=b[i]
                i=i+1
            else:
                break
        j+=1        
        return a  
    
# print(mot("abcbb"))

a=np.mat(8)
print(a)

def matrice(i,j): return [[0 for q in range(0,j)] for p in range(0,i)]
r=matrice(7,7)
print(r)

r[1]+='1'
r[1]
print(r)
