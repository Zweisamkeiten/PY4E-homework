FileName = input('Enter FileName:')

if FileName == '':
    FileName = 'mbox-short.txt'

try:
    FileHandle = open(FileName)
except:
    print('Invalid FileName')
    quit()

hour = dict()
for line in FileHandle:
    if line.startswith('From '):
        line = line.strip()
        words = line.split()
        lst_time = words[-2].split(':')
        hour[lst_time[0]] = hour.get(lst_time[0], 0) + 1
result = hour.items()
result = sorted(result)
for single, time in result:
    print(single ,time)
