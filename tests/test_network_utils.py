import unittest

from src.network_utils import analyze_ip


class TestNetworkUtils(unittest.TestCase):

    def test_private_ipv4(self):
        result = analyze_ip("192.168.1.1")

        self.assertEqual(result["version"], 4)
        self.assertTrue(result["private"])
        self.assertFalse(result["global"])

    def test_global_ipv4(self):
        result = analyze_ip("8.8.8.8")

        self.assertEqual(result["version"], 4)
        self.assertFalse(result["private"])
        self.assertTrue(result["global"])

    def test_global_ipv6(self):
        result = analyze_ip("2001:4860:4860::8888")

        self.assertEqual(result["version"], 6)
        self.assertFalse(result["private"])
        self.assertTrue(result["global"])

    def test_invalid_ip(self):
        with self.assertRaises(ValueError):
            analyze_ip("999.999.999.999")


if __name__ == "__main__":
    unittest.main()