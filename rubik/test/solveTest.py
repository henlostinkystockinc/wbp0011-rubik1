import unittest
import rubik.solve as solve 


class solveTest(unittest.TestCase):
        
        def setUp(self):
            pass
        
        def tearDown(self):
            pass
        
        
        
        #Unit Tests
        def test_check_010_FRotation(self):
            inputDict = {}
            inputDict['cube'] = ''
            inputDict['rotate'] = 'F'
            inputDict['op'] = 'solve'
            
            expectedResult = {}
            expectedResult['cube'] = ''
            expectedResult['status'] = 'ok'
            
            actualResult = solve._solve(inputDict)
            
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
        

    
    
     