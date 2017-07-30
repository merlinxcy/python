#!-*-coding:utf:8 -*-
'''
try:
    import cPickle as pickle
except ImportError:
    import pickle

d=dict(name='Bob',age=20,score=131)
dd={1:1,2:2}
print d
print dd
tmp=pickle.dumps(d)
print pickle.loads(tmp)
f=open('dump','wb')
pickle.dump(d,f)
f.close()
f=open('dump','r')
print pickle.load(f)
f.close()
'''
####
'''
import json
d=dict(name='bob',age=20,score=88)
print json.dumps(d)
'''
###
'''
from types import MethodType
class a():
    pass

def set_age(self,age):
    self.age=age

b=a()
b.set_age=MethodType(set_age,b,a)
a.name='111'
print a.name
b.set_age(1)
print b.age

class Student(object):
    __slots__=('name','age')#允许动态绑定的变量
s=Student()
s.name='michael'
s.age=25
s.score=99
'''

'''
###
class Student(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name


aaa=Student('adad')
print aaa.name
print aaa

class Fib(object):
    def __init__(self):
        self.a,self.b=0,1
    def __iter__(self):
        return self
    def next(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>10000:
            raise StopIteration()
        return self.a

for n in Fib():
    print n



class Fib2(Fib):
    def __getitem__(self,n):
        a,b=1,1
        for x in range(n):
            a,b=b,a+b
        return a

f=Fib2()
print f[0]

class Fib3(Fib2):
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b=1,1
            for x in range(n):
                a,b=b,a+b
            return a
        if isinstance(n,slice):
            start=n.start
            stop=n.stop
            a,b=1,1
            L=[]
            for x in range(stop):
                if x>=start:
                    L.append(a)
                a,b=b,a+b
            return L


print 'Fib3'
x=Fib3()
print x[:10:2]

class Student2(object):
    def __init__(self):
        self.name='self'
    def __getattr__(self,attr):
        if attr=='score':
            return 99
        raise AttributeError(attr)
S2=Student2()
print S2.name
print S2.score
#print S2.das


class Chain(object):
    def __init__(self,path=''):
        self._path=path
    def __getattr__(self,path):
        return Chain('%s/%s'%(self._path,path))
    def __str__(self):
        return self._path

print Chain()
print Chain().staus.user.timeline.list
'''

'''
class Student3():
    def __init__(self,name):
        self.name=name
        self.__pp=name
    def __call__(self):
        print self.name


s=Student3('dasd')
s()
print callable(max)
print callable(Student3)
print callable('sdasd')
'''

##type类不仅可以查询变量的类型而且还可以创建类

def fn(self,name='world'):
    print name

Hello=type('Hello',(object),dict(hello=fn))
