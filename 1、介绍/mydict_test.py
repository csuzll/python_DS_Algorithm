import unittest
from mydict import Dict

class TestDict(unittest.TestCase):

    # 测试初始化
    def test_init(self):
        d = Dict(a=1, b="test")
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, "test")
        self.assertTrue(isinstance(d, dict))

    # 测试key
    def test_key(self):
        d = Dict()
        d["key"] = "value"
        self.assertEqual(d.key, "value")

    # 测试属性
    def test_attr(self):
        d = Dict()
        d.key = "value"
        self.assertTrue("key" in d)
        self.assertEqual(d["key"], "value")

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d["empty"]

    def test_attarerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

if __name__=="__main__":
    unittest.main()