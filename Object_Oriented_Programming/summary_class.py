stuff = list() # 创建一个list类的对象
# 当python创建list对象时，首先默认自动调用类中的初始化函数，__init__
# 给对象中的值进行初始化
stuff.append('python')
stuff.append('chuck')
stuff.sort()
print(stuff[0])
# 以下两种方法等价
# 前者调用stuff中的方法__getitem__
# 后者调用list类中的方法，并把stuff对象作为地一个参数传入
print(stuff.__getitem__(0))
print(list.__getitem__(stuff, 0))

# 当不再使用对象时，stuff对象在调用__del__方法之后被析构丢弃.
# 析构方法很少被使用
#当变量被重用的那一刻，例如被重新赋值，python调用了对象里的__del__方法
# del xxxx 这样使用时__del__被自动调用
# attribute 属性， 在类中的变量

