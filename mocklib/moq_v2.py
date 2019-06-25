from mock import Mock


def _name(obj) -> str:
    return f'{obj.__module__}.{obj.__name__}'


class Patch:
    def __init__(self, func):
        self.func = func

    def __enter__(self):
        mock = Mock(self.func)
        exec(f'import {self.func.__module__}')
        exec(f'{_name(self.func)} = mock')
        return mock

    def __exit__(self, type, value, traceback):
        exec(f'import {self.func.__module__}')
        exec(f'{_name(self.func)} = self.func')


def patch(patched_func):
    def decorator(func):
        def wrapper(*args: Mock):
            with Patch(patched_func) as mock_func:
                return func(*[*args, mock_func])
        return wrapper
    return decorator










