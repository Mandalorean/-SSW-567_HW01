import unittest


class MyTestCase(unittest.TestCase):
    def test_scalene_right(self):
        from Pranav_HW01 import checkTriangle

        self.assertEqual(checkTriangle(3,4,5),"Scalene right triangle")


    def test_scalene(self):
        from Pranav_HW01 import checkTriangle

        self.assertEqual(checkTriangle(3,4,6),"Scalene triangle")


    def test_isoceles(self):
        from Pranav_HW01 import checkTriangle

        self.assertEqual(checkTriangle(4,4,5),"Isosceles triangle")


    def test_equilateral(self):
        from Pranav_HW01 import checkTriangle

        self.assertEqual(checkTriangle(5,5,5),"Equilateral triangle")


    def test_false_triangle(self):
        from Pranav_HW01 import checkTriangle

        self.assertEqual(checkTriangle(0,4,5),"Invalid triangle")







if __name__ == '__main__':
    unittest.main()
