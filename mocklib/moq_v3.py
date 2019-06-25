from contextlib import contextmanager
from mock import Mock


def _name(obj) -> str:
    return f'{obj.__module__}.{obj.__name__}'


@contextmanager
def _patch(func):
    stash = func
    try:
        mock = Mock(stash)
        exec(f'import {stash.__module__}')
        exec(f'{_name(stash)} = mock')
        yield mock
    finally:
        exec(f'{_name(stash)} = stash')


def patch(patched_func):
    def decorator(func):
        def wrapper(*args: Mock):
            with _patch(patched_func) as mock_func:
                return func(*[*args, mock_func])
        return wrapper
    return decorator










