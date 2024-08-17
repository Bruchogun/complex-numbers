import unittest
import math

from main import division
from main import addition
from main import multiplication
from main import module
from main import conjugate
from main import cartesian2polar
from main import polar2cartesian
from main import phase
from main import subtraction
from main import inputComplex

class TestStringMethods(unittest.TestCase):
    def testDivision(self):
        self.assertEqual(division([3,-6],[5,7]),[round(-27/74,4),round(-51/74,4)]) #Testing result of division
        self.assertTrue(type([]),type(division([3,-6],[5,7]))) #Testing type of result
    
    def testAddition(self):
        self.assertEqual(addition([3,-6],[5,7]),[8,1]) #Testing result of addition
        self.assertTrue(type([]),type(addition([3,-6],[5,7]))) #Testing type of result

    def testMultiplication(self):
        self.assertEqual(multiplication([3,-6],[5,7]),[57,-9])
        self.assertTrue(type([]),type(multiplication([3,-6],[5,7])))

    def testModule(self):
        self.assertEqual(module([3,-6]),round(3*(5**(1/2)),4))
        self.assertTrue(type(0),type(module([3,-6])))

    def testConjugate(self):
        self.assertEqual(conjugate([3,-6]),6)
        self.assertTrue(type(0),type(conjugate([3,-6])))

    def testCartesian2polar(self):
        self.assertEqual(cartesian2polar([3,-6]),[round(3*(5**(1/2)),4),round(math.atan2(-6,3),4)])
        self.assertTrue(type([]),type(cartesian2polar([3,-6])))
    
    def testPolar2cartesian(self):
        self.assertEqual(polar2cartesian([round(3*(5**(1/2)),4),round(math.atan2(-6,3),5)]),[3,-6])
        self.assertTrue(type([]),type(polar2cartesian([round(3*(5**(1/2)),4),round(math.atan2(-6,3),4)])))

    def testPhase(self):
        self.assertEqual(phase([3,-6]),round(math.atan2(-6,3),4))
        self.assertTrue(type(0),type(phase([3,-6])))
    
    def testSubtraction(self):
        self.assertEqual(subtraction([3,-6],[5,7]),[-2,-13])
        self.assertTrue(type([]),type(subtraction([3,-6],[5,7])))

    def testInputComplex(self):
        self.assertEqual(inputComplex('3,4'),[3,4])
        self.assertEqual(inputComplex('-3,-4'),[-3,-4])
        self.assertEqual(inputComplex('  - 3.5 , -  4.7 '),[-3.5,-4.7])

if __name__ == '__main__':
    unittest.main()