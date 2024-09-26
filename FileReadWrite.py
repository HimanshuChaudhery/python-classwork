filename = "example.txt"

# create file handle to write
file = open(filename,"w")

dataString = "Some dummy text data\n newline \t after tab"

filecontent = file.write(dataString)

file.close