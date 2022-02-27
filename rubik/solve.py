import rubik.cube as rubik
import rubik.check as check

def ClockwiseTurn(cube, indexes):
    cube = list(cube)
    cubeCopy = list(cube)
    
    faces = indexes['faces']
    for index, face in enumerate(faces, 1):
        if index != 1:
            cube[face-1] = cubeCopy[faces[index - 2]-1]
      
    edges = indexes['edges']
    for index, edge in enumerate(edges, 1):
        if index-1 % 4 == 0:
            cube[edge-1] = cubeCopy[edges[index + 2]-1] 
        else:
            cube[edge-1] = cubeCopy[edges[index - 2]-1]
      
    return "".join(cube)

def CounterClockwiseTurn(cube, indexes):
    cube = list(cube)
    cubeCopy = list(cube)
    
    faces = indexes['faces']
    for index, face in enumerate(reversed(faces), 1):
        if index != 1:
            cube[face-1] = cubeCopy[faces[index - 2]-1]
      
    edges = indexes['edges']
    for index, edge in enumerate(edges, 1):
        if index % 4 == 0:
            cube[edge-1] = cubeCopy[edges[index - 4]-1] 
        else:
            cube[edge-1] = cubeCopy[edges[index]-1]
      
    return "".join(cube)



def _solve(parms):
    
    
    
    result = {}
    encodedCube = parms.get('cube', None)       #get "cube" parameter if present
    rotates = parms.get('rotate', None)         #example rotations
    
    result['status'] = 'ok'
    
    indexesDict = {
        'F' : {'faces' : [1, 2, 3, 6, 9, 8, 7, 4, 1],
               'edges' : [10, 48, 36, 43, 13, 47, 33, 44, 16, 46, 30, 45]},
        
        'R' : {'faces' : [10, 11, 12, 15, 18, 17, 16, 13, 10],
               'edges' : [19, 54, 9, 45, 22, 51, 6, 42, 25, 48, 3, 39]},
        
        'B' : {'faces' : [19, 20, 21, 24, 27, 26, 25, 22, 19],
               'edges' : [28, 52, 18, 39, 31, 53, 15, 38, 34, 54, 12, 37]},
        
        'L' : {'faces' : [28, 29, 30, 33, 36, 35, 34, 31, 28],
               'edges' : [1, 46, 27, 37, 4, 49, 24, 40, 7, 52, 21, 43]},
        
        'U' : {'faces' : [37, 38, 39, 42, 45, 44, 43, 40, 37],
               'edges' : [12, 3, 30, 21, 11, 2, 29, 20, 10, 1, 28, 19]},
        
        'D' : {'faces' : [46, 47, 48, 51, 54, 53, 52, 48, 46],
               'edges' : [16, 25, 34, 7, 17, 26, 35, 8, 18, 27, 36, 9]}
    }
    
    for turn in rotates:
        indexes = indexesDict.get(turn.upper())
        if turn.isupper():
            encodedCube = ClockwiseTurn(encodedCube, indexes)
        elif turn.islower():
            encodedCube = CounterClockwiseTurn(encodedCube, indexes)
            
    result['cube'] = encodedCube
                 
    return result


params = {}
params['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
params['rotate'] = 'LdL'
result = _solve(params)
print("Cube " + result['cube'])