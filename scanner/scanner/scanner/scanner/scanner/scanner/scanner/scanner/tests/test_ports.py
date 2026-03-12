import unittest

from scanner.ports import parse_ports


class TestPortParsing(unittest.TestCase):
    def test_parse_single_ports(self) -> None:
        self.assertEqual(parse_ports("22,80,443"), [22, 80, 443])

    def test_parse_range(self) -> None:
        self.assertEqual(parse_ports("1-3"), [1, 2, 3])

    def test_parse_mixed(self) -> None:
        self.assertEqual(parse_ports("1-3,80,443"), [1, 2, 3, 80, 443])

    def test_invalid_port(self) -> None:
        with self.assertRaises(ValueError):
            parse_ports("70000")


if __name__ == "__main__":
    unittest.main()
