def main():
    names = ['Dean','Fanning','Mo']
    newName = input('Enter the last guest ')
    names.append(newName)
    printNames(names)
    return

def printNames(names):
    for name in names:
        print(name)
    return

main()
