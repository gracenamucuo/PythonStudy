#!/usr/bin/env python3
#-*- coding:utf-8 -*-

#print("hello,world")
print("hello,python")
#print(100 + 300)
print("The apple is a","money","哈哈哈")#单引号('')双引号（""）都可
#name = input()#输入语句
#//输入函数
#print(name)
a = 10
if a >= 0:
    print(a)
else:
    print(-a)
#python是大小写敏感
print('I\'m \"OK\"')
print(r'\\\t\\\\')#默认不转义
#print(r'''line1
#    第二行
#    第三行''')
print(3>2)
age = 19
if age >= 18:
    print('adult')
else:
    print('child')
print(None)#None表示空值
#通常用全部大写表示常量
print(10 / 3)#精确除法
print(10 // 3)#地板除
print(10 % 2)#取余数
#python的整数和浮点数都没有大小限制。超出一定范围就和直接表示inf（无限大）
#ASCII编码是1个字节，而Unicode编码通常是2个字节。随后出现的可变长编码的UTF-8编码会把一个Unicode字符根据不同的数字大小的编码成1~6个字节。常用的英文字母被编码为1个字节。汉字通常是3个字节。还有很生僻的字符编码成4~6个字节。
#在计算机内存中，统一使用Unicode编码，当保存在硬盘或者传输的时候，就转为UTF-8编码。
#ord()获取字符的整数表示
#char()把编码转换为对应的字符
print(ord('A'))
print(ord('戴'),'+',ord('运'),'+',ord('鹏'))
print(chr(65))
print('\u4e2d')
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
print('中文'.encode('utf-16'))
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print(len('ABC'))#2个字符
print(len('中文'))#3个字符
print(len(b'ABC'))#3个字节
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))#6个字节
print('This is a %s worth %d' %('apple',1000))
#list
classmates = ['xiaoming','晓红'];
print(classmates,len(classmates),classmates[0])
print(classmates[-1])#可以直接用-1做索引，取数组最后一个元素，-2，-3 依次类推
classmates.append('小白')#增加
print(classmates)
classmates.insert(1,'Jack')#插入
print(classmates)
classmates.pop()#删除末尾
print(classmates)
classmates.pop(1)#删除指定
print(classmates)
classmates[1] = '小丽'
print(classmates)
s = ['python','java',['asp','aaa'],'dd']
print(s[2][1])
#turple  元组 不可变
classmates = (1,2,3)
print(classmates)
#元祖只有一个元素时定义方法是后边加一个,
t = (1,)
print(t)

##条件判断
age  = 30
if age >= 18:
    print('成年人')
    print('哈哈哈')
else:
    print('你还小')

a = 9
if a >= 10:
    print('我大于10')
elif a == 9:
    print('我等于9')
elif a < 6:
    print('我小于6')

#s = input('birth:')
#birth = int(s)
#if birth < 2000:
#    print('00前')
#else:
#    print('00后')

sum = 0
for x in [1,2,3,2,45,56]:
    sum += x
print(sum)

print(list(range(5)))

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('END')

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)

dic = {'小明':100,'xiaohong':10,'lilei':199}
print(dic['小明'])

print('效果' in dic)
print(dic.get('效果'))
print(dic.get('效果',-1))
dic.pop('小明')
print(dic)

s = set([1,2,3,3])
print(s)
s.add(4)
print(s)
s.remove(3)
print(s)
a = ['f','d','e']
a.sort()
print(a)
t = (2,3)
dic = {t:8}
print(dic[t])
s = set([t])
print(s)
t1 = (1,[2,3])
#dic(t1:6)
#print(dic[t1])
#s1 = set([t1])
#print(s1)
#*******************************函数 *********************************************************************************
print(abs(-20))
print('最大数是:',max(2,3,5))#max()可以传入多个参数
print('数据类型转换:',int(12.33),str(1.333),bool(0),float('122.44'))
#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个别名。
a = abs
print('函数变量:',a(-2))

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print('自己定义的函数',my_abs(-99))

#空函数
def nop():
    pass

#isinstance():检查变量数据类型
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('Bad operand type')
    if x >= 0:
        return x
    else:
        return -x

#print('参数数据类型检查:',my_abs('s'))
print('参数数据类型检查:',my_abs(4))
import math
def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx,ny
r = move(100,100,50,math.pi / 6)
print(r)

def quadratic(a,b,c):
    if a == 0:
        print('a不能为0')
        return
    else:
        x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
        x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
        return x1,x2
print(quadratic(1,-2,1))

def power(x,n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(2,5))

#定义函数时，需要确定函数名和参数个数;如果有必要，可以先对参数的数据类型做检查；函数体内部可以用return随时返回函数结果;函数执行完毕也没有return语句时，自动return None；函数同时返回多个值，其实返回的是一个tuple

def enroll(name,gender,age = 6,city = 'bj'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)

enroll('小明','M',city = 'sh')#如果默认参数的位置不一样，函数调用时要把默认参数的名称写上
#默认参数必须指向不变对象！
def add_end(L = None):
    if  L is None:
        L = []
    L.append('END')
    return L

add_end()
add_end()
print(add_end())

#可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1,3,4,5))
t = (1,3,5,6,4)
print(calc(*t))#将元祖或者数组前加*变为可变参数传进去

#关键字参数 允许传入0个或任意个参数名的参数，这些关键字参数在函数内部自动组装成为一个dict  可以扩展函数的功能
#可变参数默认生成元祖，关键字参数默认生成字典
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
person('小明',88,city = 'bj')
person('好好',88, height = 289)
extra = {'city':'Beijing','job':'Engineer'}
person('好好',17,**extra)
#命名关键字参数 限制关键字参数的名字   命名关键字参数必须有参数名
def person(name,age,*,city = 'bj',job):#命名关键参数可以有默认值
    print(name,age,city,job)

person('xiaom',19,job = 'job')
#参数组合的顺序: 必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a,b,c=0,*args,**kw):
    print('a =',a,'b = ',b,'c=',c,'args=',args,'kw=',kw)

f1(*(1,2,3,4),**({'d':99,'x':'#'}))#可以自动识别元祖中的元素对应到位置参数和可变参数上
t = (1,2,3,4)
print(len(t))
def product(x,*numbers):
    pro = x
    for num in numbers:
        pro = pro * num
    return pro
print(product(4,7,2,0))

#********************************递归函数****************************
#函数调用是通过栈实现的，每当进入一个函数调用，栈就会增加一层栈帧，每当函数返回，栈就会减少一层栈帧。
#尾递归：函数返回的时候，调用自身本身，并且，return语句不能包含表达式，这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只用一个栈帧，不会出现栈溢出的情况。
#汉诺塔
def move(n,a,b,c):
    if n == 1:
        print('move',a,'--->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

#***********************切片#***********************
L = ['a','b','c','d']
L[0:3]#表示从第0个元素取到第2个元素 前闭后开 应该是 a,b,c 可以省略0 L[:3]
L[-1]#表示最后一个元素  即倒着数的第一个元素。为-1，以此类推是-2，-3
L[-3:]#L[-3:-1], -1也可以省略不写。
L[:10:2]#从前10个元素中，每两个去一个数
L[:]#复制一个数组
#元祖也可以这样切片，但是切出来 的结果依然是元祖
#字符串也可以看做list，每个元素时一个字符，可以对其进行切片操作，结果依然是字符串。
#去掉首尾空格
def trim(s):
    while(s[0] == ' '):
        s = s[1:]
    while(s[-1] == ' '):
        s = s[:-1]
    return s
#***********************迭代#***********************
from collections import Iterable#引入头文件
isinstance('abe',Iterable)#判断是否可迭代
 for i, value in enumerate(['A', 'B', 'C']):
    print(i,value)
#遍历寻找最大最小值
def findMinAndMax(L):
    min = L[0]
    max = L[0]
    for i in L:
        if i < min:
            min = i
        if i > max:
            max = i
    return(min,max)

#***********************列表生成式#***********************
>>> L = list(range(1,11))
>>> print(L)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> print([x * x for  x in range(1,11)])
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#***********************生成器(generator)***********************
#一边循环一边计算的机制
#将列表生成式的[]换为()就生成了一个生成器。
next(generator)

#杨辉三角
def sec(n):
    L = [1]
    line = 1
    while line <= n:
        yield L
        L = [1] + [L[i] + L[i+1] for i in range(len(L)-1)] + [1]
        line = line + 1
#***********************迭代器(iterator)***********************
#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。 表示一个惰性计算的序列
isinstance([2,4],Iterable)#是否可迭代
isinstance([2,4],Iterator)#是否是迭代器 生成器都是迭代器
#***********************函数式编程***********************
#高阶函数:可以接受函数作为参数的函数。
def f(c):
    return  c * c
map(f,[1,3,4])#map函数接收一个函数，和一个可迭代的对象，会将f函数作用于该可迭代对象的所有元素中，最终生成一个list
list(map(f,[1,3,4]))
#reduce函数也接收两个参数，一个是函数，一个是序列，函数必须接受两个参数，reduce把结果继续和序列的下一个元素做累计计算。例如:reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

#数字字符串转数字
 DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
 def str2int(s):
    def fn(x,y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn,map(char2num,s))
#首字母小写，其他大写
L = ['adam', 'LISA', 'barT']
def lowerFirst(L):
    s1 = L[0]
    s1 = s1.lower()
    
    s2 = L[1:]
    s2 = s2.upper()
    return s1 + s2

print(list(map(lowerFirst,L)))

from functools import reduce
def pro(x,y):
    return x * y

reduce(pro(),[1,2,3,4,5])


def f1(s):
    i = 0
    total = len(s)
    a = True
    while i < (total + 1) / 2:
        if s[i] == s[total-i-1]:
            a = True
        else:
            a = False
                break;
    return a

def f2(x):
    s = str(x)
    if f1(s):
    return x
SyntaxError: expected an indented block
 def f2(x):
    s = str(x)
    if f1(s):
        return x

#排序
from operator import itemgetter
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
sorted(L,key=itemgetter(0))
sorted(L,key=itemgetter(1))

#函数作为参数返回  --->闭包
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1,2,4,5)

# ******返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

#匿名函数
list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))#关键字lambda表示匿名函数，冒号前面的x表示函数参数。 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：

#装饰器
#函数对象有一个__name__属性，可以拿到函数的名字
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
#偏函数
import functools
int2 = functools.partial(int, base=2)
#返回的int2函数和 下边的函数效果一样
def int2(x, base=2):
    return int(x, base)
















































































































































