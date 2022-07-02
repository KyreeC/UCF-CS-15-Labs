path = input("Enter a directory path for the text file: ")
filename = input("Enter full filename: ")
file = open(path+"\\"+filename, "r")
#File structure will differ based on OS

for line in file:
    print(line)

file.close()

input("\n Press 'Enter' to exit program")
#Prevents program from closing upon execution