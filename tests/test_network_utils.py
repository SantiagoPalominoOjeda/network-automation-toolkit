import unittest

from src.network_utils import analyze_ip
from src.network_utils import scan_network

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

    def test_scan_network(self):
        results = scan_network("192.168.1.0/30")

        self.assertEqual(len(results), 2)
        self.assertIn("192.168.1.1", results)
        self.assertIn("192.168.1.2", results)


if __name__ == "__main__":
    unittest.main()