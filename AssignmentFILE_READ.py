# WAP to read a data from csv file and store the data in two dimensional list.

fileName = "Data.csv"

# function to read csv file and return list.
def read_csv(fileName):

    ext = fileName.split(".")[-1].lower()
    assert ext =="csv","Invalid file type"

    fileHandle = open(fileName,"r")
    data = fileHandle.read()
    fileHandle.close()

    #logic
    rows = data.split("\n")
    # print(rows)
    for i in range(0,len(rows)):
        row = rows[i]
        rows[i] = row.split(",")

    # print("\n")
    # print(row)

    # return data
    op = rows
    return op # it should return list of list 

receivedData = read_csv(fileName)

print(receivedData)

