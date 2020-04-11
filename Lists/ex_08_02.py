FileName = input("Enter FileName:")
if FileName == "":
    FileName = "romeo.txt"

try:
    FileHandle = open(FileName)
except:
    print("Invalid FileName")
    quit()

lst = list()
for line in FileHandle:
    #print(line.strip())
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)
