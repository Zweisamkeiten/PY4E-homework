# 面向对象的编程的真正能量在于能够用一个类构建多个实例
# 当我们构建同一个类的多个实例时，我们可能想要给不同的对象以不同# 的初始值
class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'part count', self.x)

    def __del__(self):
        print(self.name, 'is destructed')

s = PartyAnimal('Sally')
j = PartyAnimal('Jim')

s.party()
j.party()
s.party()
