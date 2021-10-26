newFile = open("demo.txt", "w")

lines = [
    "Hello! Welcome to demo.txt\n",
    "This file is for testing purposes.\n",
    "Good Luck!\n",
]
for line in lines:
    newFile.write(line)  # write by line
newFile.close()

try:
    print('Trying to open "dem0.txt" (not "demo.txt")')
    readFile = open("dem0.txt")
except OSError as e:
    print(e)
    print()

readFile = open("demo.txt")
for line in readFile:
    print(line, end="")  # read by line

readFile.readline()  # read until line end or EOF
readFile.readline(5)  # read N bytes (characters) or until line end or EOF
readFile.readlines()  # read lines from file as lines list
readFile.readlines(5)  # read N lines from file as lines list

readFile.close()

print("\n@@@@@@@@@@@@@@@@@@@@@@\n")

newFile = open("demo.txt", "w")
newFile.writelines(lines)  # write lines array
newFile.close()

with open("demo.txt") as readFile:  # using 'with' statement to control resources
    print(readFile.read())  # read whole content

print("\n@@@@@@@@@@@@@@@@@@@@@@\n")

with open("./small_projects/1. conditions/calculator.py") as f:
    print(f.read())

print("\n@@@@@@@@@@@@@@@@@@@@@@\n")

with open("./small_projects/1. conditions/calculator.py", encoding="utf-8") as f:
    print(f.read())

print("\n@@@@@@@@@@@@@@@@@@@@@@\n")

with open("./small_projects/1. conditions/calculator.py", mode="rb") as f:
    text = f.read()
    print("Original")
    print(text)
    # print("ASCII")
    # print(text.decode("ascii"))
    print("UTF-8")
    print(text.decode("utf-8"))
    print("UTF-16")
    print(text.decode("utf-16"))
    print("CP1251")
    print(text.decode("cp1251"))
