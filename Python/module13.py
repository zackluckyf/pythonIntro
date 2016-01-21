userInput = int(input('Enter your total purchase: '))
if userInput < 50:
    userInput += 10
print('Your total is $%d' %userInput)
