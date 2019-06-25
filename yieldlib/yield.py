
def generate_data():
    for data in range(10):
        yield data


def do_stuff():
    print('first')
    yield 0
    print('second')
    yield 1
    print('third')
    yield


def try_next(it):
    try:
        return True, next(it)
    except:
        return False, None


n = do_stuff()

while next(n) is not None:
    print('client')
