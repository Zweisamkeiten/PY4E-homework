FileName = input("Enter FileName:")

if FileName == "":
    FileName = "mbox-short.txt"

try:
    FileHandle = open(FileName)
except:
    print("Invalid FileName")
    quit()

count = 0
for line in FileHandle:
    if line.startswith("From "):
        words = line.split()
        print(words[1])
        count += 1

print("There were", count, "lines in the file with From as the first word")
