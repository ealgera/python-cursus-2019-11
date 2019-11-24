import zipfile

my_zipfile = zipfile.ZipFile("data.zip", "r")

print(my_zipfile.namelist())
#for item in my_zipfile.namelist():
#    print(item)

my_zipfile.close()

#with zipfile.ZipFile("data.zip", "r") as myzip:
#    print(myzip.namelist())

#with zipfile.ZipFile("data.zip", "r") as myzip:
#    myzip.extractall("Data")