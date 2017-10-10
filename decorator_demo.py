from functools import wraps

# 装饰器实际上就是一个函数
# 有两个特别之处
# 1. 参数是一个函数
# 2. 返回值是一个函数


# 在所有函数打印之前，先打印一个分割线

# 1. 装饰器使用通过@符号，放在函数上面
# 2. 装饰器中定义的函数，要使用*args,**kwargs两个兄弟组合。并且在函数中执行原始函数的时候，也要把*args,**kwargs传进去
# 3. 需要使用functools.wraps在装饰器中的函数上把传进来的这个函数进行包裹，这样就不会丢失原来函数的__name__等属性

def my_log(func):

    @wraps(func)
    def ret(*args,**kwargs):
        print('---------------')
        func(*args,**kwargs)

    return ret

@my_log
def run():
    print('run')

@my_log
def add(a,b):
    print('结果是：%d' % (a+b))


if __name__ == '__main__':
    print(run.__name__)
    run()
    add(1,2)