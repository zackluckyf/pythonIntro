fileName = 'demo.txt'
WRITE = 'w'
READ = 'r'
APPEND = 'a'
READWRITE = 'w+'

#lets user write data to a file
data = input('Please enter file info: ')
file = open(fileName, mode = WRITE)
file.write(data)
file.close

#inputs preset things to a file
#myfile = open(fileName, mode = WRITE)
#myfile.write('Susan, 29\n')
#myfile.write('Christopher, 31\n')
#myfile.write('')
#myfile.close()

print('File written successfully')

