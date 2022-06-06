import inspect
import sys
def get_functions():
    list=inspect.getmembers(sys.modules[__name__], \
        predicate = lambda f: inspect.isfunction(f) and f.__module__ == __name__)
    dictionary = dict(('user_'+x, y) for x, y in list)
    dictionary.pop("user_get_functions")
    return dictionary

#======================
#User-defined-functions
#======================
