import re


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

with open('1/input2.txt') as f:
    lines = f.readlines()
    total = 0
    for line in lines:
        numbers = re.findall(r'(one|two|three|four|five|six|seven|eight|nine|\d)', line)
        transformed = []
        for number in numbers:
            if (number != ''):
                transformed.append(word2num(number))
                
        if (len(transformed) > 0):
            lineNumber = transformed[0] * 10 + transformed[len(transformed)-1]
            total += lineNumber
            #print(lineNumber)
            #print(line)
        else:
            print("No result?")
    print(total)
    
    


