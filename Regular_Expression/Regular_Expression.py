import re

FileName = input('Enter FileName:')

if FileName == '':
    FileName = './regex_sum_372414.txt'

try:
    FileHandle = open(FileName)
except:
    print('Invalid FileName')
    quit()

total = 0
for line in FileHandle:
    #re.search('[0-9]+', line) 返回搜索到的位置
    number_list = re.findall('[0-9]+', line)
    if len(number_list) >= 1:
        for number in number_list:
            total += int(number)
print(total)

