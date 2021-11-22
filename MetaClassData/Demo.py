# -*- coding: utf-8 -*-

class MetaClass(type):

    def __new__(mcs, *args, **kwargs):
        print("MetaClass::__new__")
        return type.__new__(mcs, *args, **kwargs)

    def __init__(cls, *args, **kwargs):
        print("MetaClass::__init__")
        super(MetaClass, cls).__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        print("MetaClass::__call__")
        return type.__call__(cls, *args, **kwargs)


class DemoClass(metaclass=MetaClass):

    def __new__(cls, *args, **kwargs):
        print("DemoClass::__new__")
        return super(DemoClass, cls).__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        print("DemoClass::__init__")
        super(DemoClass, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        print("DemoClass::__call__")


d = DemoClass()
d()
