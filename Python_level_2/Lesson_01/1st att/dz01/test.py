
import json
import unittest
from unittest.mock import Mock
import lib

class CTest(unittest.TestCase):

    def test_1(self):

        res = lib.div(20, 4)

        self.assertEqual(res, 5.0)

    def test_2(self):

        self.assertRaises(AssertionError, lib.div, 5, 0)

    def test_3(self):

        res = \
        {
            "+" : 30
        }
        res_json = json.dumps(res)
        res_buf = res_json.encode()

        virt_sock = Mock()
        virt_sock.send.return_value = None # __call__
        virt_sock.recv.return_value = res_buf

        result = lib.main_loop_for_server(virt_sock)

        self.assertEqual(result["+"], res["+"])

