from unittest import TestCase
import rubik.solve as solve 
import unittest

class SolveTest(TestCase):
        
    def test_check_010(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
                'solution':'FfRrBbLlUuDd'}
        result = solve._solve(parm)

        status = result.get('status', None)
        self.assertEqual(status, 'ok')


        
if __name__ == '__main__':
    unittest.main()    