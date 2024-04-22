class A:
    def run(self):
        print("A can run")

    def jump(self):
        print("A can Jump")


class B:
    def run(self):
        print("B can run")

    def jump(self):
        print("B can jump")

def meth(obj):
    obj.run()
    obj.jump()

a=A()
b=B()
meth(a)
meth(b)