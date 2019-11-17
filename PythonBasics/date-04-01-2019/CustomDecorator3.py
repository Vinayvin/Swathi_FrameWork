class Custom_decorator():

    def __init__(self, f):
        print("from __init__()")
        f() # Prove that function definition has completed

    def __call__(self):
        print("from __call__()")

@Custom_decorator
def Function():
    print("inside aFunction()")

print("Finished decorating aFunction()")

Function()