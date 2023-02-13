# Работа с файлом

FILE = 'pi.txt'

with open(FILE) as file_object:
    contents = file_object.read()

print(contents.rstrip())

with open(FILE) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(FILE) as file_object:
    lines = file_object.readlines()

print(lines)
for l in lines:
    print(l.rstrip())
