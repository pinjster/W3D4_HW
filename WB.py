# Pair of Gloves

# Winter is approaching, and you are preparing for your ski holidays. Your task is to determine the number of pairs of gloves you can create from the gloves in your drawer.

# Given an array describing the color of each glove, your goal is to calculate the number of pairs you can make. Remember, only gloves of the same color can form pairs.

# Write a function that takes in the array of glove colors and returns the number of pairs that can be constituted.

# Examples:

# Input :
glove1 = ["red", "green", "red", "blue", "blue"]

# Output: 2
# **Explanation:**
# You can form 1 pair of red gloves and 1 pair of blue gloves.


# Input:
glove = ["red", "red", "red", "red", "red", "red"]

# Output: 3

# Explanation:
# You can form 3 pairs of red gloves.

glove2 = ["red", "green", "red", "blue", "blue", "orange","purple", "aquamarine"]
glove3 = ["red", "blue", "orange"]
glove4 = []

def pair(gloves):
    return int(len(list(filter(lambda x: len([num for num in gloves if num == x]) // 2 != 0 , gloves))) / 2)

print(pair(glove1))
print(pair(glove))
print(pair(glove2))
print(pair(glove3))
print(pair(glove4))
print(pair(["red","red","red","blue","blue","blue"]))