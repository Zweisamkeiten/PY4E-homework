# 将partyanimal类单独放入party.py文件，从已有父类 扩展 子类
from party import PartyAnimal

# 当定义Cricketfan时，即为在扩展父类partyanimal
# 这意味着父类的x变量, party方法都被继承到cricketfan中
class CricketFan(PartyAnimal):
    points = 0
    def six(self):
        self.points = self.points + 6
        self.party()
        print(self.name, 'points', self.points)

s = PartyAnimal('Sally')
s.party()
print(dir(s))
j = CricketFan('Jim')
j.party()
j.six()
# 相较于父类，子类cricketfan中有另外的能力
print(dir(j))
