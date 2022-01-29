import rubik.cube as rubik

def _check(parms):
    result={}
    encodedCube = parms.get('cube', None)       
    if(encodedCube == None):
        result['status'] = 'error: Cube Empty'
    elif(type(encodedCube) != 'str'):
        result['status'] = 'error: Incorrect Type'
    elif(len(encodedCube) != 54):
        result['status'] = 'error: Incorrect Number of Elements'
    else:
        colorAmounts = {}
        
        
        result['status'] = 'ok'
    return result