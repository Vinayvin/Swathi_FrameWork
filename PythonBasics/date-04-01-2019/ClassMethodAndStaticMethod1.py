class Class1:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

ob=Class1()
print(ob.method())
# print(MyClass.method())
print(ob.classmethod())
print(Class1.classmethod())
print(ob.staticmethod())
print(Class1.staticmethod())