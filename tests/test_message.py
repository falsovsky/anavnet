import unittest
from anavnet.anavnet import AnavNet


class TestMessage(unittest.TestCase):
    def setUp(self):
        self.anavnet = AnavNet()
        self.anavnet.set_port(16)

    def test_get_message_no_port(self):
        anavnet = AnavNet()
        with self.assertRaises(RuntimeError):
            anavnet.get_message(1)

    def test_get_total_messages_no_port(self):
        anavnet = AnavNet()
        with self.assertRaises(RuntimeError):
            anavnet.get_total_messages()

    def test_get_message_invalid_index_small(self):
        with self.assertRaises(IndexError):
            self.anavnet.get_message(0)

    def test_get_message_invalid_index_big(self):
        with self.assertRaises(IndexError):
            self.anavnet.get_message(self.anavnet.get_total_messages() + 1)


if __name__ == '__main__':
    unittest.main()
