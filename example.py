class MyBaseClass:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f'Hello, {self.name}!')


class DerivedClass(MyBaseClass):
    def __init__(self, first_name):
        super().__init__(first_name)
        self.chase = first_name

    def go(self):
        return self.display()


myDerivedClass = DerivedClass('Chase')

myDerivedClass.go()
print(myDerivedClass.name)
