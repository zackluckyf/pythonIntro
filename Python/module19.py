#arrays let you store values
guests = ['Christopher','Susan','Zack','Mo']
#prints guests
for listnum in range(4):
    print(guests[listnum])
print('******')
#dean added and then printed
guests.append('Dean')
for listnum in range(5):
    print(guests[listnum])
#mo and christopher removed and then printed
guests.remove('Mo')
del guests[0]
print('******')
for listnum in range(3):
    print(guests[listnum])
print('******')
#special loop that iterates over every element
for currentGuest in guests:
    print(currentGuest)
print('******')
#sorts into alphabetical order and then prints it
guests.sort()
for currentGuest in guests:
    print(currentGuest)