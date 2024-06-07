def readCSV(file : str) -> list:
    result = [] 

    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            splitstr = line.split(',')
            result.append(list(map(float, splitstr)))

    return result