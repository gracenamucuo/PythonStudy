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














