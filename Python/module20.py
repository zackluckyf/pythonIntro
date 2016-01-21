#asks the user for the number of guests
print('How many people are attending the party? ')
numGuests = input()
numGuests = int(numGuests)
names = []
#has the user enter the names of the guests
print('Enter their names: ')
for guests in range(numGuests):
    names.append(input())
print('******')
#sorts the guests alphabetically and then prints the list
names.sort()
for currentGuest in names:
    print(currentGuest)

