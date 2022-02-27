import unittest
import rubik.cube as cube 


class solveTest(unittest.TestCase):
        
        def setUp(self):
            pass
        
        def tearDown(self):
            pass
        
        
        
        #Unit Tests
        def test_init(self):
            myCube = cube.Cube()
            self.assertIsInstance(myCube, cube.Cube)
        
        def test_load(self):
            pass
        
        def test_get(self):
            pass
        
        

    
    