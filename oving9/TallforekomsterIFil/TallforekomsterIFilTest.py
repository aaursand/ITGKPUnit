import unittest
from TallforekomsterIFil import *

class TallforekomstTester(unittest.TestCase):
    def test_a(self):
        self.assertEqual(number_of_lines("numbers.txt"), 36, "number_of_lines returnerte ikke riktig antall linjer for numbers.txt")
        self.assertEqual(number_of_lines("numbers2.txt"), 0, "number_of_lines returnerte ikke riktig antall linjer for numbers2.txt")

    def test_b(self):
        demNums = number_frequency("numbers.txt")
        demNums2 = number_frequency("numbers2.txt")
        self.assertEqual(demNums[7], 4, "ikke riktig antall 7ere")
        self.assertEqual(demNums[1], 3, "ikke riktig antall 1ere")
        self.assertEqual(demNums[8], 1, "ikke riktig antall 8ere")
        self.assertTrue(0 not in demNums, "0 forekommer ikke i numbers.txt")
        self.assertEqual(demNums2, {}, "numbers2 er en tom fil, men number_frequency returnerer ikke en tom dictionary")






if __name__ == "__main__":
    unittest.main()
