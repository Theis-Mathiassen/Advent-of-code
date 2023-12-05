import re

class Map:
    def __init__ (self, ranges_str):
        self.ranges = len(ranges_str)
        self.destination = []
        self.source = []
        self.length = []
        for range in ranges_str:
            values = re.findall(r'\d+', range)
            if (len(values) != 0):
                self.destination.append(int(values[0]))
                self.source.append(int(values[1]))
                self.length.append(int(values[2]))
    def Transform (self, value):
        for i in range(len(self.destination)):
            if (value >= self.source[i] and value < self.source[i] + self.length[i]):
                return value + (self.destination[i]-self.source[i])
        return value
        


with open('5/input.txt') as f:
    lines = f.readlines()
    Maps = []
    seeds = []
    lowest = float('inf')
    segments = []
    segment = []
    for line in lines:
        if (line == "\n"):
            print(f'Appending segment: {segment[0]}')
            segments.append(segment)
            segment = []
        else:
            segment.append(line)
    if (len(segment) != 0):
        segments.append(segment)
    
            
    for i, segment in enumerate(segments):
        if (i == 0):
            seeds = re.findall(r'\d+', segment[0])
        else:
            Maps.append(Map(segment))


    for seed in seeds:
        value = int(seed)
        for map in Maps:
            print(f'{value} -> ', end='')
            value = map.Transform(value)
        print(value)
        lowest = value if value < lowest else lowest


    
    
    print(lowest)
