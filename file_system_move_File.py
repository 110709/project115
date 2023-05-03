import os

source = "C:/Users/avika/Downloads/main.txt.txt"
dest = "C:/Users/avika/Downloads/newfile.txt.txt"

os.rename(source, dest)
print("Source path renamed to destination path successfully.")