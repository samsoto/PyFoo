from mock import Mock


def _name(obj) -> str:
    return f'{obj.__module__}.{obj.__name__}'


def patch(patched_func):
    def decorator(func):
        def wrapper(*args: Mock):
            stash = patched_func
            try:
                mock_func = Mock(patched_func)
                exec(f'import {stash.__module__}')
                exec(f'{_name(stash)} = mock_func')
                result = func(*[*args, mock_func])
            finally:
                exec(f'{_name(stash)} = stash')
            return result
        return wrapper
    return decorator
