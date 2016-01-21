fileName = 'tasmania.txt'

#open my file with read/write access
animalFile = open(fileName, mode = 'w+')

animalFile.write('Cat\n')
animalFile.write('Dog\n')
animalFile.write('Emu\n')
animalFile.write('Horse\n')
animalFile.write('Leopard\n')

animalFile.seek(0)
firstAnimal = animalFile.readline()
print(firstAnimal)

secondAnimal = animalFile.readline()
print(secondAnimal)

animalFile.seek(0)
allFileContents = animalFile.read()

print(allFileContents)