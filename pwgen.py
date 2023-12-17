import random
print("Welcome to the Password Generator!")

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefughijklmnopqrstuvwxyz!@#$%^&*().,;'"

num = input("Amount of generated passwords you want: ")
num = int(num)

# line 6 asks for user input
# line 7 converts the input from line 6 into an integer

length = input('Input desired password length: ')
length = int(length)

# line 12 asks for user input
# line 13 converts given input into integer

print("Here are your generated passwords: ")

for pw in range(num):
    passwords = " "
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)

# for loop lines 20-23 are to print random pws. range in num will print generated pws from given input
# for loops lines 20-23 random.choice is from import random in line 1. choices random symbols for chars var