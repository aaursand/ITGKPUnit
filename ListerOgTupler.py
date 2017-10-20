import unittest
















































class ListTupleTester(unittest.TestCase):
    def subtest_a(self):
        a = GetRandomNumbers(100, 1, 10)
        if not len(a) == 100:
            return False
        for e in a:
            if e < 1 or e > 10:
                return False
        return True

    def test_a(self):
        self.assertTrue(self.subtest_a(), "GetRandomNumbers returnerte ikke en liste med de attributter forventet.")

    def test_b(self):
        self.assertEqual(HowManyN([1, 5, 5, 5, 3, 3, 2, 5], 5), 4, "HowManyN returnerte ikke riktig antall forekomster.")

    def test_c(self):
        self.assertEqual(HowManyN((1,5,5,5,3,3,2,5), 5), 4, "HowManyN returnerte ikke riktig antall forekomster i tuplen.")

    def test_d(self):
        self.assertEqual(summate([5,5,5,5,2]), 22, "summate returnerte ikke riktig sum.")

    def test_e(self):
        self.assertEqual(sorter([4,5,3]), [3,4,5], "sorter returnerte ikke den sorterte listen.")

    def test_g(self):
        self.assertEqual(mode([2,3,4,3,2,2,4]), 2, "mode returnerte ikke typetallet.")

    def test_h(self):
        self.assertEqual(reverse([1,2,3]), [3,2,1], "reverse returnerte ikke den reverserte listen.")


if __name__ == '__main__':
    unittest.main()
