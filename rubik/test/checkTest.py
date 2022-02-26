from unittest import TestCase
import rubik.check as check 
import unittest

class CheckTest(TestCase):
        
    def test_check_010_ShouldReturnOkOnSolvedCube(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
    def test_check_010_ShouldReturnOkOnSolvedCubeDisorganized(self):
        parm = {'op':'check',
                'cube':'yybbbbbbbrrrrwrrrggggrrggggoooooooooyyybyyybywwwwgwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')

    def test_check_020_ReturnErrorOnNull(self):
        parm = {'op':'check',
                'cube': None}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: Cube Empty')

    def test_check_030_ReturnErrorOnIncorrectTypeInt(self):
        parm = {'op':'check',
                'cube': 42}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: Incorrect Type')
        
    def test_check_030_ReturnErrorOnIncorrectTypeFloat(self):
        parm = {'op':'check',
                'cube': 3.4}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: Incorrect Type')
        
    def test_check_030_ReturnErrorOnIncorrectTypeBool(self):
        parm = {'op':'check',
                'cube': True}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: Incorrect Type')
        
    def test_check_040_ReturnErrorOnTooManyElements(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: Incorrect Number of Elements')
        
    def test_check_040_ReturnErrorOnTooFewElements(self):
        parm = {'op':'check',
                'cube':'bbbbbbbrrrrrrrgggggggoooooooyyyyyyyyyyyyyyyy'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: Incorrect Number of Elements')
   
    def test_check_050_ReturnErrorOnIncorrectColorAmounts(self):
        parm = {'op':'check',
                'cube':'yybbbbbbbrrrrrrrrrrrgggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: Need 9 Occurrences of 6 Colors')
        
    def test_check_060_ReturnErrorOnDuplicateCenter(self):
        parm = {'op':'check',
                'cube':'gbbbbbbbrrrrrbrrrrggggbggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: Matching Center Squares')
        
    def test_check_070_ReturnErrorOnSpecialChars(self):
        parm = {'op':'check',
                'cube':'@@@@@@@@@rrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: No Special Characters Allowed for Color')
        
if __name__ == '__main__':
    unittest.main()     