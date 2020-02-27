import unittest
import task


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def test1_getArea(self):
        radius = 5.6
        result = task.getArea(radius)
        self.assertEqual(98.53, result)

    def test2_getArea(self):
        radius = 3
        result = task.getArea(radius)
        self.assertNotEqual(3, result)


if __name__ == '__main__':
    unittest.main()
