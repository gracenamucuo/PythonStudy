class Animal(object):
        def run(self):
            print('Animal is running')

def run_teice(animal):
        animal.run()
        animal.run()
#对于Python这样的动态语言来说，不一定需要传入Animal类型，只需要保证传入的对象有一个run()方法就可以。
#判断一个变量是不是某个类型
isinstance(a,Animal)
#判断对象类型，使用type()函数:
#type()函数返回的是Class类型

#判断一个对象是否是函数
import types
    def fn():
    pass

type(fn)==types.FunctionType
True
type(abs)==types.BuiltinFunctionType
True
type(lambda x: x)==types.LambdaType
True
type((x for x in range(10)))==types.GeneratorType
True
#配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
class MyObject(object):
     def __init__(self):
         self.x = 9
     def power(self):
         return self.x * self.x

 obj = MyObject()

 hasattr(obj, 'x') # 有属性'x'吗？
True
 obj.x
9
 hasattr(obj, 'y') # 有属性'y'吗？
False
 setattr(obj, 'y', 19) # 设置一个属性'y'
 hasattr(obj, 'y') # 有属性'y'吗？
True
 getattr(obj, 'y') # 获取属性'y'
19
 obj.y # 获取属性'y'
19

#类属性归类所有，但是所有该类的实例都可以访问到。

class Stu(object):
    pass
s = Stu()
s.name = '添加属性名字'
#绑定方法
#实例绑定方法
def set_age(self,age):
    self.age = age
from types import MethodType
s.set_age = MethodType(set_age,s)
s.set_age(5)
#类绑定方法
def set_score(self,score):
    self.score = score
Stu.set_score = set_score
#对实例的属性进行限制 只允许Stu实例添加name和age属性
class Stu(object):
    __slots__ = ('name','age')#用tuple定义绑定的属性名称
#__slots__仅是对当前类实例起作用，对继承的子类不起作用
#@property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。
#类设计的时候，通常主线是单一继承下来的，但是要‘混入’额外功能的时候，通过多继承就可以实现，为了更好地看出继承关系，一般把非主线的继承名字后缀加上MixIn
#定制类
# __str__ 类似 重写OC类中description方法
class Stu(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'Stu object (name: %s) ' % self.name

print(Stu('你好'))
#Stu object (name: 你好
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__
#如果想一个类可以for……in 循环 需要实现一个__iter__()方法，方法返回一个迭代对象，还需要在该类中实现一个__next__()方法 直到遇到StopIteration

# __call__ 我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象

 def fn(self,name='world'):
    print('Hello , %s.' % name)


 Hello = type('Hello',(object,),dict(hello=fn))

#要创建一个class对象，type()函数需要传入3个参数:
#class的名称
#继承的父类的机会，Python支持多继承，如果只有一个父类，也要写成tuple的单元素的写法。
#class的方法名称与函数绑定，上述列子我们把函数fn绑定到方法名hello()上。















































