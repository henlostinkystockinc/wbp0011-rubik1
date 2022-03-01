class Cube:
    '''
    Rubik's cube
    '''

    def __init__(self):
        self.cube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        self.rotates = ''
        self.op = ''
    
    def load(self, cube, rotates, op):
        self.cube = cube
        self.rotates = rotates
        self.op = op
    
    def get(self):
        parms = {}
        parms['cube'] = self.cube
        parms['rotates'] = self.rotates
        parms['op'] = self.op
        return parms


