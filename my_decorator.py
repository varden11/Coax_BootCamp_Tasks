def my_decorator(func):
    def wrapper():
        print('do something before call of func')
        func()
        print('do something after call of func')
    return wrapper

def hello():
    print ('hello world')

some_func_decorated = my_decorator(hello)
some_func_decorated()
