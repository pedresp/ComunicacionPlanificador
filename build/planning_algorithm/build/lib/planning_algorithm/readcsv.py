def readUAV():
    f = open('UAV.csv', 'r')
    lines = f.readlines()

    result = []

    for line in lines:
        result.append(line[:-1].split(','))
        result[-1] = list(map(float, result[-1]))    
    
    return result