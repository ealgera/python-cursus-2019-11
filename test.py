import zipfile

with (zipfile.ZipFile("data.zip", "r")) as my_zipfile:

    # for item in my_zipfile.namelist():
    # print(item)
    my_zipfile.extractall("Data")

# my_zipfile.close()
