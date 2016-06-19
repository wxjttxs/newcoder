#!/usr/bin/python
 #coding:utf-8
'''
def log(func):
    def wrapper(*args,**kvargs):
        #*无名参数    hello('xiaojing',2)
        #**有名参数
        print 'before calling',func.__name__
        print 'args',args,'kvargs',kvargs
        func(*args,**kvargs)
        print 'end calling',func.__name__
    return wrapper

@log
def hello(name,age):
    print 'hello',name,age
'''

def log(level,*args, **kvargs):
    def inner(func):

        def wrapper(*args, **kvargs):
            print level,'before calling', func.__name__
            print level,'args', args, 'kvargs', kvargs
            func(*args, **kvargs)
            print level,'end calling', func.__name__
        return wrapper
    return inner

@log(level='INFO')
def hello(name,age):
    print 'hello',name,age

if __name__=='__main__':
    #hi()
    #hello('xiaojing',2)
    hello(name='xiaojing',age=2)