import re

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

def word2num (str):
    if (str == "one"):
        return 1
    elif (str == "two"):
        return 2
    elif (str == "three"):
        return 3
    elif (str == "four"):
        return 4
    elif (str == "five"):
        return 5
    elif (str == "six"):
        return 6
    elif (str == "seven"):
        return 7
    elif (str == "eight"):
        return 8
    elif (str == "nine"):
        return 9
    else:
        return int(str)

symbols = ["one","two","three","four","five","six","seven","eight","nine","1","2","3","4","5","6","7","8","9"]

with open('1/input2.txt') as f:
    lines = f.readlines()
    total = 0
    for line in lines:
        number_indexes = [0] * len(line)
        for symbol in symbols:
            finds = list(find_all(line, symbol))
            for found in finds:
                number_indexes[found] = word2num(symbol)
        transformed = []
        for value in number_indexes:
            if (value != 0):
                transformed.append(value)
        if (len(transformed) > 0):
            lineNumber = transformed[0] * 10 + transformed[len(transformed)-1]
            total += lineNumber
            print(lineNumber)
            print(line)
        else:
            print("No result?")
    print(total)
    
    


