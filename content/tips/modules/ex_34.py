import sys
import types


def some_function():
    print('Hello, World!')


some_attribute = 1


class ThisModule(types.ModuleType):
    some_attribute = 0

    def some_function(self):
        print(self)


sys.modules[__name__] = ThisModule(__name__)
