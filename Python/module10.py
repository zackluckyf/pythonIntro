import datetime
today = datetime.date.today()
userInput = input('Enter the project deadline(mm/dd/yyyy)')
deadline = datetime.datetime.strptime(userInput, '%m/%d/%Y').date()
days = deadline - today
print('You have ')
print(days)
print('To get the project done')



