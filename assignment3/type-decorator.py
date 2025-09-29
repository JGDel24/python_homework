def type_converter(type_of_output):
    def decorator(func):
        def wrapper(*args, **kwargs):
            x = func(*args, **kwargs)

            return type_of_output(x)
        return wrapper
    return decorator

@type_converter(str)
def return_int():
    return 5

@type_converter(int)
def return_string():
    return 'not a number'

if __name__ == '_main_':
    y = return_int()
    print(type(y).__name__)


