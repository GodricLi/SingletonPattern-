# _*_ coding=utf-8 _*_
"""单例模式"""

# 1.使用模块:
"""Python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，
当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码。
因此，我们只需把相关的函数和数据定义在一个模块中，就可以获得一个单例对象了。"""

# class Singleton(object):
#
#     def foo(self):
#         pass
#
#
# singleton = Singleton()

# 将上面的代码保存在文件 mysingleton.py 中，要使用时，直接在其他文件中导入此文件中的对象，这个对象即是单例模式的对象
# from mysingleton import singleton

# 2.使用元类metaclass
"""
1.类由type创建，创建类时，type的__init__方法自动执行，类实例化，执行type的 __call__方法
2.对象由类创建，创建对象时，类的__init__方法自动执行，对象()执行类的 __call__ 方法
"""


# class Singleton(type):
#     """
#     在元类Singleton的__call__方法对类属性__instance进行判断，如果__instance为None，
#     说明类还未进行实例化，那么调用元类的父类（元类是type的子类）type的__call__方法，
#     同时赋值给 cls.__instance。如果 cls.__instance 不为None，
#     说明类已经进行过实例化，直接返回之前存储在类属性cls.__instance 中的类实例，即实现单例模式。
#     """
#     def __init__(cls, *args, **kwargs):
#         cls.__instance = None
#         super().__init__(*args, **kwargs)
#
#     def __call__(cls, *args, **kwargs):
#         if not cls.__instance:
#             cls.__instance = super().__call__(*args, **kwargs)
#         return cls.__instance
#
#
# class Foo(metaclass=Singleton):
#     pass
#
#
# foo1 = Foo()
# foo2 = Foo()
# print(foo1 is foo2)

# 3.使用__new__方法
# class Singleton(object):
#     """当我们实例化一个对象时，是先执行了类的__new__方法（我们没写时，默认调用object.__new__），
#     实例化对象,然后再执行类的__init__方法，对这个对象进行初始化，
#     所有我们可以基于这个，实现单例模式"""
#
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, '_instance'):  # 关键在于每一次实例化，我们都返回这同一个_instance对象
#             cls._instance = super().__new__(cls)
#         return cls._instance
#
#
# class Foo(Singleton):
#     def __init__(self):
#         pass
#
#
# foo1 = Foo()
# foo2 = Foo()
# print(foo2 is foo1)

# 4.使用装饰器
def singleton(cls):
    instance = {}

    def get_singleton(*args, **kwargs):
        if cls not in instance:                     # 判断是否存在字典中
            instance[cls] = cls(*args, **kwargs)    # 这里相当于Foo()
        return instance[cls]

    return get_singleton


@singleton
class Foo:
    pass


foo1 = Foo()
foo2 = Foo()
print(foo1 is foo2)
