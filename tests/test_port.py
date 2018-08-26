import unittest
from anavnet import AnavNet


class TestPort(unittest.TestCase):
    def test_set_port_invalid(self):
        anavnet = AnavNet()
        with self.assertRaises(KeyError):
            anavnet.set_port(666)

    def test_get_port_name(self):
        anavnet = AnavNet()
        port = 34
        anavnet.set_port(port)
        self.assertEqual(anavnet.get_port_name(), anavnet.get_ports()[port])

    def test_get_port_name_not_set(self):
        anavnet = AnavNet()
        with self.assertRaises(RuntimeError):
            anavnet.get_port_name()


if __name__ == '__main__':
    unittest.main()
