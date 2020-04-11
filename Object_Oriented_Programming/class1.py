class PartAnimal:
    x = 0
#考虑对象的生命周期，需要考虑其建立和销毁。
    #当python构建一个对象时，他先调用__init__方法，使得我们有机会初始化对象的默认值
    #class类中内置__init__ __del__方法，这样是增加内容
    def __init__(self): # self 是创建的对象的alias代号
        print('I am constructed')

    def party(self):
        self.x = self.x + 1
        print('So far', self.x)

    def __del__(self):
        print('I am destructed', self.x)

an = PartAnimal()
# 每当python创建一个partyanimal类的对象，它就会调用__init__去给对象初始化值与数据
print('Type', type(an))
#print('Dir', dir(an))
#print('Type', type(an.x))
#print('Type', type(an.party))
an.party()
an.party()
an = 42 #当变量被重用的这一刻，python调用了对象里的__del__方法
#print(type(an)) #重新定义后类型是int而不是原来的partAnimal类
#print('an ccontains', an)
#PartAnimal.party(an)  #与an.party()等价
