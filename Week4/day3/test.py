import unittest
import extend

class TestExtend(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_3_and_3_is_6(self):
        self.assertEqual(extend.add(3, 3), 6)

    def test_add_3_and_7_is_10(self):
        self.assertEqual(extend.add(3, 7), 10)

    def test_max_of_three_first(self):
        self.assertEqual(extend.max_of_three(5, 4, 10), 10)

    def test_max_of_three_secound(self):
        self.assertEqual(extend.max_of_three(20, 40, 17), 40)

    def test_median_four(self):
        self.assertEqual(extend.median([7,5,3,5]), 5)

    def test_median_five(self):
        self.assertEqual(extend.median([1,2,3,4,5]), 3)

    def test_is_vovel_a(self):
        self.assertTrue(extend.is_vovel('a'))

    def test_is_vovel_ú(self):
        self.assertTrue(extend.is_vovel('ú'))

    def test_is_vovel_u(self):
        self.assertTrue(extend.is_vovel('u'))

    def test_translate_bemutatkozik(self):
        self.assertEqual(extend.translate('bemutatkozik'), 'bevemuvutavatkovozivik')

    def test_translate_kolbice(self):
        self.assertEqual(extend.translate('kolbice'), 'kovolbiviceve')

    def test_translate_kolbice(self):
        self.assertEqual(extend.translate('teve'), 'teveveve')

if __name__ == '__main__':
    unittest.main()