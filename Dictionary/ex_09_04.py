FileName = input("Enter FileName:")

if FileName == '':
    FileName = 'mbox-short.txt'

try:
    FileHandle = open(FileName)
except:
    print("Invalid FileName")
    quit()

committers = dict()
for line in FileHandle:
    if line.startswith('From '):
        words = line.split()
        committers[words[1]] = committers.get(words[1], 0) + 1

Bigcommitter = None
Bigtime = None
for committer, time in committers.items():
    if Bigcommitter == None or time > Bigtime:
        Bigcommitter = committer
        Bigtime = time

print(Bigcommitter, Bigtime)


