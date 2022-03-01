import rubik.check as check

def ClockwiseTurn(cube, indexes):
    cube = list(cube)
    cubeCopy = list(cube)
    
    faces = indexes['faces']
    for index, face in enumerate(faces, 1):
        index = index - 1
        if index % 4 == 0:
            cube[face-1] = cubeCopy[faces[index + 3]-1] 
        else:
            cube[face-1] = cubeCopy[faces[index - 1]-1]
      
    edges = indexes['edges']
    for index, edge in enumerate(edges, 1):
        index = index - 1
        if index % 4 == 0:
            cube[edge-1] = cubeCopy[edges[index + 3]-1] 
        else:
            cube[edge-1] = cubeCopy[edges[index - 1]-1]
      
    return "".join(cube)

def CounterClockwiseTurn(cube, indexes):
    cube = list(cube)
    cubeCopy = list(cube)
    
    faces = indexes['faces']
    for index, face in enumerate(faces, 1):
        index = index - 1
        if (index+1) % 4 == 0:
            cube[face-1] = cubeCopy[faces[index - 3]-1] 
        else:
            cube[face-1] = cubeCopy[faces[index + 1]-1]
      
    edges = indexes['edges']
    for index, edge in enumerate(edges, 1):
        index = index - 1
        if (index+1) % 4 == 0:
            cube[edge-1] = cubeCopy[edges[index - 3]-1] 
        else:
            cube[edge-1] = cubeCopy[edges[index + 1]-1]
      
    return "".join(cube)



def _solve(parms):
    
    result = check._check(parms)
    
    if result['status'] == 'ok':
        encodedCube = parms.get('cube', None)       #get "cube" parameter if present
        rotates = parms.get('rotate', None)         #example rotations
    
        indexesDict = {
            'F' : {'faces' : [1, 3, 9, 7, 2, 6, 8, 4],
                   'edges' : [10, 48, 36, 43, 13, 47, 33, 44, 16, 46, 30, 45]},
        
            'R' : {'faces' : [10, 12, 18, 16, 11, 15, 17, 13],
                   'edges' : [19, 54, 9, 45, 22, 51, 6, 42, 25, 48, 3, 39]},
        
            'B' : {'faces' : [19, 21, 27, 25, 20, 24, 26, 22],
                   'edges' : [28, 52, 18, 39, 31, 53, 15, 38, 34, 54, 12, 37]},
        
            'L' : {'faces' : [28, 30, 36, 34, 29, 33, 35, 31],
                   'edges' : [1, 46, 27, 37, 4, 49, 24, 40, 7, 52, 21, 43]},
        
            'U' : {'faces' : [37, 39, 45, 43, 38, 42, 44, 40],
                   'edges' : [12, 3, 30, 21, 11, 2, 29, 20, 10, 1, 28, 19]},
        
            'D' : {'faces' : [46, 48, 54, 52, 47, 51, 53, 49],
                   'edges' : [16, 25, 34, 7, 17, 26, 35, 8, 18, 27, 36, 9]}
        }
        
        if rotates == '':
            rotates = 'F'
        
        for turn in rotates:
            if turn.upper() in indexesDict:
                indexes = indexesDict.get(turn.upper())
                if turn.isupper():
                    encodedCube = ClockwiseTurn(encodedCube, indexes)
                elif turn.islower():
                    encodedCube = CounterClockwiseTurn(encodedCube, indexes)
                result['cube'] = encodedCube
                print(encodedCube + "Turn " + turn)      
            else:
                result['status'] = 'error: Unknown Rotates Provided'
                result['cube'] = ''
                
                 
        return result


params = {}
params['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
params['rotate'] = 'uLfD'
result = _solve(params)