import os

#prompt user to change directory
dirme = input("Enter a directory:".strip())
os.chdir(dirme)
listining = os.listdir(dirme)

#Create file to write to
output = open("write.txt", "w")

#iterate throug directory
for i in listining:
    input = open(i, "r")
    for lines in input:
        output.write(lines)
    input.close()
    output.write("\n")
output.close()

#Remove files
for i in listining:
    if(i != "write.txt"):
        os.remove(i)