
def service(req: int) -> str:
    data = dao(req)
    return response(data)


def dao(req) -> list:
    return list(range(req))


def response(data: list) -> str:
    return str(len(data))


def foo(x: int, y: int, z: int) -> int:
    return x * y * z
