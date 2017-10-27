import unittest
from Bursdagsdatabasen import *

class BirthdayTester(unittest.TestCase):
    def test_a(self):
        add_birthday_to_date("12 jan", "Sindre")

    def test_b(self):
        add_birthday_to_date("9 feb", "Lillian")

if __name__ == "__main__":
    unittest.main()
