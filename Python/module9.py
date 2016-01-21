import datetime

today = datetime.date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.strftime('%d %b, %Y'))

userInput = input('Please enter your next birthday(mm/dd/yyyy): ')
birthday = datetime.datetime.strptime(userInput, '%m/%d/%Y').date()
print(birthday)
days = birthday - today
print(days)
