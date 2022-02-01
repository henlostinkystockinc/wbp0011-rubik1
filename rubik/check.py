import rubik.cube as rubik

def _check(parms):
    result={}
    encodedCube = parms.get('cube', None)       
    if(encodedCube == None):
        result['status'] = 'error: Cube Empty'
    elif(type(encodedCube) != str):
        result['status'] = 'error: Incorrect Type'
    elif(len(str(encodedCube)) != 54):
        result['status'] = 'error: Incorrect Number of Elements'
    else:
        
        colorAmounts = {} #Dictionary Keeping track of Colors as keys with amount of each color on cube
        
        for index, color in enumerate(encodedCube):
            
            #Checks if index correlates with a center square
            if (index-4) % 9 == 0:
                centerSquare = True
            else:
                centerSquare = False
            
            #Check if color added to dictionary already
            if color in colorAmounts:
                
                #Is there too many of that color. At maximum there can only be 9 of a single color
                if colorAmounts.get(color)[0] == 9:
                    result['status'] = 'error: Need 9 Occurrences of 6 Colors'
                    return result
                else:
                    #Checks to see if current color is already a center square on another face of the cube
                    if colorAmounts[color][1] and centerSquare:
                        result['status'] = 'error: Matching Center Squares'
                        return result
                    colorAmounts[color][0] = colorAmounts[color][0] + 1
                    if centerSquare:
                        colorAmounts[color][1] = centerSquare
            else:
                
                #Are there too many colors. At maximum there can only be 6 colors
                if len(colorAmounts) == 6:
                    result['status'] = 'error: Need 9 Occurrences of 6 Colors'
                    return result
                else:
                    colorAmounts[color] = [1, centerSquare]
                    
                                       
        
        
        result['status'] = 'ok'
    return result