from mocklib import module
from mocklib import moq_v2 as moq
from unittest.mock import Mock
import unittest


class RmTestCase(unittest.TestCase):

    @moq.patch(module.dao)
    @moq.patch(module.response)
    def test_moq(self, dao: Mock, response: Mock):
        dao.return_value = [1]
        response.return_value = 1
        result = module.service(10)
        print(result)
