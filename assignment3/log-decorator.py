import logging
from functools import wraps

logger = logging.getLogger(__name__ + '_parameter_log')
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler('./decorator_log', 'a'))

def logger_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        pos_args = args if args else 'none'
        kw_kwargs = args if args else 'none'

        result = func(*args, **kwargs)

        log_message = (
            f'function: {func._name_}\n'
            f'positional parameter: {pos_args}\n'
            f'keyword parameter: {kw_kwargs}\n'
            f'return: {result}\n'
        )

        logger.info(log_message)

        return result
    return wrapper

@logger_decorator
def greet():
    print("Hello, World!")
@logger_decorator
def check_all_true(*args):
    return all(args) 

@logger_decorator
def return_decorator(**kwargs):
    print("Returning the decorator itself.")
    return logger_decorator

if __name__ == '_main_':
    greet()
    check_all_true(True, 1, "non-empty")
    return_decorator(name="Alice", language="Python")

 


    