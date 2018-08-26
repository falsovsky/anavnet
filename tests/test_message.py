import unittest
from anavnet import AnavNet


class TestMessage(unittest.TestCase):
    def test_get_message_no_port(self):
        anavnet = AnavNet()
        with self.assertRaises(RuntimeError):
            anavnet.get_message(1)

    def test_get_total_messages_no_port(self):
        anavnet = AnavNet()
        with self.assertRaises(RuntimeError):
            anavnet.get_total_messages()

    def test_get_message_invalid_index(self):
        anavnet = AnavNet()
        anavnet.set_port(16)
        with self.assertRaises(IndexError):
            anavnet.get_message(anavnet.get_total_messages() + 1)


if __name__ == '__main__':
    unittest.main()
