def func1():
    def func2():
        var1 = 0  # shouldn't be extracted as func name
        pass
    pass


def func3():
    pass


print(42)


# the rest shouldn't be extracted as func name

var2 = 1


class Class1():
    pass


class1 = Class1
