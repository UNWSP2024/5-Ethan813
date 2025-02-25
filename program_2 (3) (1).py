# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# ------

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.
def add_numbers(n1, n2):
    sum = n1 + n2
    return sum
number1 = 206
number2 =42
print(number1,'+',number2,'=')
answer = float(input())
sum = add_numbers(number1, number2)
print(sum)
if answer == sum:
    print('correct, the answer is:', sum)
else:
    print('incorrect, the correct answer is:', sum)
    #ethan collins 2/17/2025 quiz