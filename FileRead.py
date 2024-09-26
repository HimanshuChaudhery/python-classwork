filename = "example.txt"

# create file handle to write
file = open(filename,"r")


filecontent = file.read()
print(filecontent)

# close and save file
file.close