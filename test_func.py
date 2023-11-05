import unittest


class MyTestCase(unittest.TestCase):
    def test_1(self):
        assert list(map(lambda x: x + 10, [1, 2, 3, 4, 5])) == [11, 12, 13, 14, 15]

    def test_2(self):
        assert list(filter(lambda x: x > 5, [2, 7, 1, 8])) == [7, 8]

    def test_3(self):
        assert sorted([3, 1, 4, 1, 6]) == [1, 1, 3, 4, 6]

    def test_4(self):
        from math import pi
        assert abs(pi - 3.1416) < 0.00001

    def test_5(self):
        from math import sqrt
        assert [sqrt(n ** 2) for n in range(10)] == [n for n in range(10)]

    def test_6(self):
        from math import pow
        assert [pow(n, m) for n in range(1, 11) for m in range(1, 11)] == [n ** m for n in range(1, 11) for m in
                                                                           range(1, 11)]

    def test_7(self):
        from math import hypot
        assert [hypot(3, 4), hypot(5, 12), hypot(8, 15)] == [5, 13, 17]

if __name__ == '__main__':
    unittest.main()
