'''
    Lesson: Input and F Strings
    Author: Mr. Kalisz
    Date Created: Sept 14, 2024
    Date Last Modified: Sept 14, 2024
'''

#Input - how to send information to the program

#input() #Program to stop here until the user types something in and presses enter

#Prompt - Message tell the user what you expect them to do

#input("Insert your name: ") #If this is not stored in a variable, whatever is typed is gone

answer = input("Input your name: ") #Stores our input in answer
#Input always saves as a String - Strings can hold any character

print("name: " + answer)

#F Strings - String formatting


word = "Hello World"
word2 = f"{word} Bye World"
#easier to read
combinedWords = f"Words before my variables {word} then {word2} Type more"
#combinedWords = "Words before my variables " + word + " then " + word2 + " Type more"

print(combinedWords)

num= 99
print(f"my number is: {num}") #F strings can take any data type of variable

