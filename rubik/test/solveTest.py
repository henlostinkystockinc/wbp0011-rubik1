import unittest
import rubik.solve as solve 


class solveTest(unittest.TestCase):
        
        def setUp(self):
            pass
        
        def tearDown(self):
            pass
        
        
        
        #Unit Tests
        def test_check_Blank_Rotation_00_01(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = ''
            inputDict['op'] = 'solve'
            
            expectedResult = {}
            expectedResult['cube'] = 'bbbbbbbbbyrryrryrrgggggggggoowoowoowyyyyyyooorrrwwwwww'
            expectedResult['status'] = 'ok'
            
            actualResult = solve._solve(inputDict)
            
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            
        def test_check_Wrong_Rotation_00_02(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 'RrH'
            inputDict['op'] = 'solve'
            
            expectedResult = {}
            expectedResult['cube'] = ''
            expectedResult['status'] = 'error: Unknown Rotates Provided'
            
            actualResult = solve._solve(inputDict)
            
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            
        def test_check_F_Rotation_01_01(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 'F'
            inputDict['op'] = 'solve'
            
            expectedResult = {}
            expectedResult['cube'] = 'bbbbbbbbbyrryrryrrgggggggggoowoowoowyyyyyyooorrrwwwwww'
            expectedResult['status'] = 'ok'
            
            actualResult = solve._solve(inputDict)
            
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            
        def test_check_f_Rotation_01_02(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 'f'
            inputDict['op'] = 'solve'
            
            expectedResult = {}
            expectedResult['cube'] = 'bbbbbbbbbwrrwrrwrrgggggggggooyooyooyyyyyyyrrrooowwwwww'
            expectedResult['status'] = 'ok'
            
            actualResult = solve._solve(inputDict)
            
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            
        def test_check_Ff_Rotation_01(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 'Ff'
            inputDict['op'] = 'solve'
            
            expectedResult = {}
            expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            expectedResult['status'] = 'ok'
            
            actualResult = solve._solve(inputDict)
            
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
           
           
           
           
           
        def test_check_R_Rotation_02_01(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 'R'
            inputDict['op'] = 'solve'
            
            expectedResult = {}
            expectedResult['cube'] = 'bbwbbwbbwrrrrrrrrryggyggyggoooooooooyybyybyybwwgwwgwwg'
            expectedResult['status'] = 'ok'
            
            actualResult = solve._solve(inputDict)
            
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            
        def test_check_r_Rotation_02_02(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 'r'
            inputDict['op'] = 'solve'
            
            expectedResult = {}
            expectedResult['cube'] = 'bbybbybbyrrrrrrrrrwggwggwggoooooooooyygyygyygwwbwwbwwb'
            expectedResult['status'] = 'ok'
            
            actualResult = solve._solve(inputDict)
            
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            
        def test_check_Rr_Rotation_02(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 'Rr'
            inputDict['op'] = 'solve'
            
            expectedResult = {}
            expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            expectedResult['status'] = 'ok'
            
            actualResult = solve._solve(inputDict)
            
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
     
     
     
     
     
        def test_check_L_Rotation_03_01(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 'L'
            inputDict['op'] = 'solve'
            
            expectedResult = {}
            expectedResult['cube'] = 'ybbybbybbrrrrrrrrrggwggwggwooooooooogyygyygyybwwbwwbww'
            expectedResult['status'] = 'ok'
            
            actualResult = solve._solve(inputDict)
            
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            
        def test_check_l_Rotation_03_02(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 'l'
            inputDict['op'] = 'solve'
            
            expectedResult = {}
            expectedResult['cube'] = 'wbbwbbwbbrrrrrrrrrggyggyggyooooooooobyybyybyygwwgwwgww'
            expectedResult['status'] = 'ok'
            
            actualResult = solve._solve(inputDict)
            
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            
        def test_check_Ll_Rotation_03(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 'Ll'
            inputDict['op'] = 'solve'
            
            expectedResult = {}
            expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            expectedResult['status'] = 'ok'
            
            actualResult = solve._solve(inputDict)
            
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            
 
 
 
 
        def test_check_B_Rotation_04_01(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 'B'
            inputDict['op'] = 'solve'
            
            expectedResult = {}
            expectedResult['cube'] = 'bbbbbbbbbrrwrrwrrwgggggggggyooyooyoorrryyyyyywwwwwwooo'
            expectedResult['status'] = 'ok'
            
            actualResult = solve._solve(inputDict)
            
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            
        def test_check_b_Rotation_04_02(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 'b'
            inputDict['op'] = 'solve'
            
            expectedResult = {}
            expectedResult['cube'] = 'bbbbbbbbbrryrryrrygggggggggwoowoowoooooyyyyyywwwwwwrrr'
            expectedResult['status'] = 'ok'
            
            actualResult = solve._solve(inputDict)
            
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))           
            
        def test_check_Bb_Rotation_04(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 'Bb'
            inputDict['op'] = 'solve'
            
            expectedResult = {}
            expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            expectedResult['status'] = 'ok'
            
            actualResult = solve._solve(inputDict)
            
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
        
        
        
        
        def test_check_U_Rotation_05_01(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 'U'
            inputDict['op'] = 'solve'
            
            expectedResult = {}
            expectedResult['cube'] = 'rrrbbbbbbgggrrrrrroooggggggbbbooooooyyyyyyyyywwwwwwwww'
            expectedResult['status'] = 'ok'
            
            actualResult = solve._solve(inputDict)
            
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            
        def test_check_u_Rotation_05_02(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 'u'
            inputDict['op'] = 'solve'
            
            expectedResult = {}
            expectedResult['cube'] = 'ooobbbbbbbbbrrrrrrrrrgggggggggooooooyyyyyyyyywwwwwwwww'
            expectedResult['status'] = 'ok'
            
            actualResult = solve._solve(inputDict)
            
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
        def test_check_Uu_Rotation_05(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 'Uu'
            inputDict['op'] = 'solve'
            
            expectedResult = {}
            expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            expectedResult['status'] = 'ok'
            
            actualResult = solve._solve(inputDict)
            
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))





        def test_check_D_Rotation_06_01(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 'D'
            inputDict['op'] = 'solve'
            
            expectedResult = {}
            expectedResult['cube'] = 'bbbbbbooorrrrrrbbbggggggrrroooooogggyyyyyyyyywwwwwwwww'
            expectedResult['status'] = 'ok'
            
            actualResult = solve._solve(inputDict)
            
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            
        def test_check_d_Rotation_06_02(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 'd'
            inputDict['op'] = 'solve'
            
            expectedResult = {}
            expectedResult['cube'] = 'bbbbbbrrrrrrrrrgggggggggooooooooobbbyyyyyyyyywwwwwwwww'
            expectedResult['status'] = 'ok'
            
            actualResult = solve._solve(inputDict)
            
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            
        def test_check_DdRotation_06(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 'Dd'
            inputDict['op'] = 'solve'
            
            expectedResult = {}
            expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            expectedResult['status'] = 'ok'
            
            actualResult = solve._solve(inputDict)
            
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            
            
            
            
            
        def test_check_AllRotation_07(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 'FfRrLlBbUuDd'
            inputDict['op'] = 'solve'
            
            expectedResult = {}
            expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            expectedResult['status'] = 'ok'
            
            actualResult = solve._solve(inputDict)
            
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            
            
            
        def test_check_RandRotation_08_01(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 'fUR'
            inputDict['op'] = 'solve'
            
            expectedResult = {}
            expectedResult['cube'] = 'wrobbwbbwwwgrrgrrgyoyyggyggbbbooyooyryrrybryboogwwgwwo'
            expectedResult['status'] = 'ok'
            
            actualResult = solve._solve(inputDict)
            
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            
        def test_check_RandRotation_08_02(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 'DLLrFl'
            inputDict['op'] = 'solve'
            
            expectedResult = {}
            expectedResult['cube'] = 'rgrybbyyywrbyrbgrbwgowgwwrwywbgoogoogyroygyogbrrbwbowo'
            expectedResult['status'] = 'ok'
            
            actualResult = solve._solve(inputDict)
            
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            
        def test_check_RandRotation_08_03(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 'uLfD'
            inputDict['op'] = 'solve'
            
            expectedResult = {}
            expectedResult['cube'] = 'rbbrbbooowggwrryyyoowggwrrrooyooyggwgyygyygrrbbbwwbwwb'
            expectedResult['status'] = 'ok'
            
            actualResult = solve._solve(inputDict)
            
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            
        def test_check_RandRotation_08_04(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
            inputDict['rotate'] = 'FlFLfLurDRdB'
            inputDict['op'] = 'solve'
            
            expectedResult = {}
            expectedResult['cube'] = 'rorybwgrrbbobrwgybggyggrwbrogbyooyoobrwyyoygwywwwwbgro'
            expectedResult['status'] = 'ok'
            
            actualResult = solve._solve(inputDict)
            
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
            
