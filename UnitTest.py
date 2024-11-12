from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testCases = {1: ([[1,2],[3,2],[2,4],[5,6],[3,5]], [1,2,3,4,5,6], [2,4,5,5,6,6]),
                            2: ([[1,2],[1,2],[1,3],[1,4]], [1], [4]),
                            3: ([[10,1000]], [5], [0])}
        self.__obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_Case1(self):
        items, queries, output = self.__testCases[1]
        result = self.__obj.maximumBeauty(items = items, queries = queries)
        self.assertIsInstance(result, list)
        self.assertTrue(all(x == y for x, y in zip(result, output)))

    @timeout(0.5)
    def test_Case2(self):
        items, queries, output = self.__testCases[2]
        result = self.__obj.maximumBeauty(items = items, queries = queries)
        self.assertIsInstance(result, list)
        self.assertTrue(all(x == y for x, y in zip(result, output)))

    @timeout(0.5)
    def test_Case3(self):
        items, queries, output = self.__testCases[3]
        result = self.__obj.maximumBeauty(items = items, queries = queries)
        self.assertIsInstance(result, list)
        self.assertTrue(all(x == y for x, y in zip(result, output)))

if __name__ == '__main__':
    unittest.main()