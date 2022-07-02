import os


try:
    os.mkdir(r"C:\Users\krizz\Downloads\Cars")
except:
    print("This directory already exists")
with open(r"C:\Users\krizz\Downloads\Cars\Mustang.txt", "a+") as file:
    pass

path = input("Enter directory path: ")
FileName = input("Enter file name: ")
NewName = input("Enter a new name: ")

os.system(r"copy {}\{} {}\{}".format(path, FileName, path, NewName))
