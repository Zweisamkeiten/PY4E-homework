FileName = input("Enter Name:")

try:
    FileHand = open(FileName)
except:
    print("Invalid FileName")
    quit()

count = 0
total = 0
for line in FileHand:
    if line.startswith('X-DSPAM-Confidence:'):
        dotpos = line.find('.')
        count += 1
        total += float(line[dotpos - 1:])

average = total / count

print("Average spam confidence:", average)

