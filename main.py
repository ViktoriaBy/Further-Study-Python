# Create a function called helloWorld which simply prints ‘Hello, World!’

def helloworld():
    print("Hello World!")


helloworld()


# Create a function called printName which takes in a person’s name and console logs it.
# Call the function, passing in an argument.

def printName():
    print('Viktoria')


printName()


# Create a function called greeting that accepts name as its only parameter.
# greeting should log the string ‘Hello, ‘ plus the value of the name parameter.
# Make sure to call your function and pass in an argument.

def greeting(name):
    print('Hello ' + name)


greeting('Lola')


# Create a function called add that takes in two parameters (both of these will be numbers).
# The add function should RETURN the two parameters added together.
# Create a variable outside the function called ‘sum’ and set it equal to add invoked (called), passing in 2 arguments.

def add(n1, n2):
    return n1 + n2


sum = add(2, 2)

print(sum)


# Write a function called nameCheck that takes in a name parameter.
# nameCheck should check if the name equals ‘Steven’. If it does, return ‘What is up Steven?’
# If the name parameter is equal to Bryan, return ‘Hey Bryan!’
# If the name parameter is anything else,
# return ‘Cool name, NAMEPARAM’ (with NAMEPARAM being the value of the name parameter being passed in).
# Create a variable called ‘nameGreeting’ and set it equal to your function invoked (called) passing in an argument.

def nameCheck(name):
    if name == 'Steven':
        print('What is up Steven?')
    elif name == 'Bryan':
        print('Hey Bryan!')
    else:
        print(f'Cool name, {name}')


nameCheck('Viki')


# Write a function called faveColorFinder that takes in one parameter called color (which will be a string).
# If the passed in color equals ‘red’, return ‘red is a great color’.
# If the passed in color equals ‘green’, return ‘green is a solid favorite color’.
# If the passed in color equals ‘black’, return ‘so trendy’.
# Otherwise, you should return the string ‘you need to evaluate your favorite color choice’.
# Create a variable called ‘colorRating’ and set it equal to faveColorFinder invoked (called), passing in an argument.

def faveColorFinder(color):
    if color == 'red':
        print('red is a great color')
    elif color == 'green':
        print('green is a solid favorite color')
    elif color == 'black':
        print('so trendy')
    else:
        print('You need to evaluate your favorite color choice')


faveColorFinder('green')


# Create a function called printAllNames that takes in a single argument (a list of names).
# Using a for loop, iterate over that list and print each name. Call the function, passing in a list of names.

def printAllNames(myList):
    for name in myList:
        print(name)


printAllNames(['Jon', 'Jim'])


# Create a function called thatsOdd that takes in a single argument (a number).
# Using conditional logic, if the number is even, return ‘That’s not odd!’.
# Otherwise, return ‘That is odd indeed!’.
# Outside the function, create a variable called oddChecker and set it equal to your function invoked,
# making sure to pass in an argument.

def thatsOdd(num):
    if num % 2 == 0:
        print("That's not odd!")
    else:
        print('That is odd indeed!')


thatsOdd(21)

#Create a function called ‘bigOrSmall’ that takes in one parameter, ‘nums’,
#which will be an list of numbers. Inside of the bigOrSmall function, create a new list called ‘answers’.
# Then, loop over the passed in nums parameter, and check to see if the number in the list is GREATER than 100.
# If it is, push ‘big’ as a string to the answers list.
# If the number is LESS than or EQUAL to 100, push ‘small’ as a string to the answers list.
# Return the answers list inside of the function to a variable called listEvaluator.
# Outside the function, create a variable called bigSmallResults and set it equal
# to your function invoked, making sure to pass in an argument.

def bigOrSmall(nums):
    answers = []
    for num in nums:
        if num > 100:
            answers.append('big')
        elif num <= 100:
            answers.append('small')
    print(answers)
    listEvaluator = answers


bigSmallResults = bigOrSmall([5,6,10,110,130,150,2,20,40,200])


#Write a function that is called theEliminator, which takes in two arguments,
# contestants (which will each be an list of strings), and loser (which will be a string).
# The function should loop over the list of contestant names.
# If the loser string appears in the list, take it out.
# Return the new contestants list.
# - Example list: contestants = [‘Katniss’, ‘Peeta’, ‘Fox-face’, ‘Glimmer’, ‘Cato’, ‘Rue’, ‘Thresh’, ‘Clove’, ‘Marvel’] - Example string: loser = ‘Glimmer’


def theEliminator(contestants, loser):
    for contestant in contestants:
        if loser == contestant:
            contestants.remove(loser)
    return contestants

contestants = ['Katniss', 'Peeta', 'Fox-face', 'Glimmer', 'Cato', 'Rue', 'Thresh', 'Clove', 'Marvel']
loser = 'Glimmer'

print(theEliminator(contestants, loser))