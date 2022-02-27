import unittest
import rubik.cube as cube 


class solveTest(unittest.TestCase):
        
        def setUp(self):
            pass
        
        def tearDown(self):
            pass
        
        
        
        #Unit Tests
        def test_init():
        	myCube = cube.Cube()
        	self.assertIsInstance(myCube, cube.Cube)
        	
        def test_load():
        	pass
        	
        def test_get():
        	pass
        
        

    
    
     