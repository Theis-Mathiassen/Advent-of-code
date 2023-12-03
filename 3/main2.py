






# Make a list of all numbers, and a matrix where each index is what number is on that position.
# Then for each * lookup the matrix that only 2 different ids is next to it. Get those numbers 
# from the list and multiply them together and add to total.

with open('3/input.txt') as f:
    lines = f.readlines()
    total = 0
    schematic = []
    number_matrix_index = []
    number_values = []
    number_amount = 0
    width = 140
    height = 140
    for line in lines:
        schematic_line = []
        indexes = []
        for char in line:
            schematic_line.append(char)
            indexes.append(-1)
        schematic.append(schematic_line)
        number_matrix_index.append(indexes)
    
    for idy, line in enumerate(lines):
        cur_num_str = ''
        for idx, char in enumerate(line):
            if (char.isdigit()):
                cur_num_str = cur_num_str + char
            else:
                if cur_num_str != '':
                    cur_num = int(cur_num_str)
                    number_values.append(cur_num)
                    for b in range(idx-len(cur_num_str), idx):
                        number_matrix_index[idy][b] = number_amount
                    cur_num_str = ''
                    number_amount += 1
    
    for idy, line in enumerate(lines):
        for idx, char in enumerate(line):
            if (char == '*'):
                numbers_touching = []
                for j in range(-1, 2):
                    for i in range(-1, 2):
                        x = i+idx
                        y = j+idy
                        if (x >= 0 and y >= 0 and x < width and y < height):
                            if (number_matrix_index[y][x] != -1 and not(number_matrix_index[y][x] in numbers_touching)):
                                numbers_touching.append(number_matrix_index[y][x])
                if (len(numbers_touching) == 2):
                    total += number_values[numbers_touching[0]] * number_values[numbers_touching[1]]



    print(number_matrix_index[139])
    print(number_values[1220])



                
    print(total)