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
            myCube = cube.Cube()
            myCube.load('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww', 'Rr', 'solve')
            self.assertIsInstance(myCube, cube.Cube)
            self.assertEqual('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww', myCube.cube)
            self.assertEqual('Rr', myCube.rotates)
            self.assertEqual('solve', myCube.op)
                
                        
        def test_get(self):
            myCube = cube.Cube()
            myCube.load('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww', 'Rr', 'solve')
            cubeParms = myCube.get()
            self.assertIsInstance(myCube, cube.Cube)
            self.assertEqual('bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww', cubeParms.get('cube'))
            self.assertEqual('Rr', cubeParms.get('rotates'))
            self.assertEqual('solve', cubeParms.get('op'))
        
        

    
    