


with open('3/input.txt') as f:
    lines = f.readlines()
    total = 0
    schematic = []
    width = 140
    height = 140
    for line in lines:
        schematic_line = []
        for char in line:
            schematic_line.append(char)
        schematic.append(schematic_line)
    
    for idy, line in enumerate(lines):
        cur_num = 0
        cur_num_str = ''
        cur_num_start = 0
        cur_num_finish = 0
        active_num = False
        for idx, char in enumerate(line):
            if (char.isdigit()):
                if active_num == False:
                    active_num = True
                    cur_num_start = idx
                cur_num_str = cur_num_str + char
                #print("(" + str(idx) + ", " + str(idy) + ") = " + char)
            else:
                if active_num == True:
                    #Check if number is adjacent to symbol and add it.
                    cur_num_finish = idx-1
                    active_num = False
                    cur_num = int(cur_num_str)

                    part_of_schematic = False
                    for j in range(idy-1, idy+2):
                        for i in range(cur_num_start-1, cur_num_finish+2):
                            if (i>= 0 and j >= 0 and i < width and j < height and schematic[j][i].isdigit() == False and schematic[j][i] != '.'):
                                part_of_schematic = True
                    if (part_of_schematic):
                        total += cur_num
                        #print(cur_num)
                    cur_num_str = ''
    print(total)