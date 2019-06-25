from mock import Mock
from mocklib import module
from mocklib import moq_v1 as moq


@moq.patch(module.dao)
@moq.patch(module.response)
def test(dao: Mock, response: Mock):
    dao.return_value = [1]
    response.return_value = 1
    result = module.service(10)
    print(result)


print('--------------')
res = module.service(10)
print(res)

print('--------------')
test()

print('--------------')
res = module.service(10)
print(res)

