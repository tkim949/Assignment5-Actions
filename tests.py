import unittest
import task
# from datetime import date


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
    '''
    def test1_getElementList(self):
        testList1 = [1, 2, 3, 4, 5, 6, 0]
        gotList = task.getElementList(testList1)
        self.assertEqual(1, gotList[0])
        self.assertEqual(0, gotList[-1])

    def test2_getElementList(self):
        testList2 = ['apple', 'banana', 'orange', 'mango', 'grape']
        gotList = task.getElementList(testList2)
        self.assertNotEqual('banana', gotList[0])
        self.assertNotEqual('apple', gotList[-1])

    def test1_getdaysBWdates(self):
        date1 = date(2011, 4, 8)
        date2 = date(2020, 2, 27)
        days = task.daysBWdates(date1, date2)

        self.assertEqual(3247, days)

    def test2_getdaysBWdates(self):
        date1 = date(2020, 2, 25)
        date2 = date(2020, 2, 27)

        days = task.daysBWdates(date1, date2)

        self.assertNotEqual(10, days)
    '''


if __name__ == '__main__':
    unittest.main()
