import re

with open('4/input.txt') as f:
    lines = f.readlines()
    total = 0
    for line in lines:
        card, numbers = line.split(":")
        card_number = int(re.findall(r'\d+', card)[0])
        my_numbers_str, winning_numbers_str = numbers.split('|')
        my_numbers = re.findall(r'\d+', my_numbers_str)
        winning_numbers = re.findall(r'\d+', winning_numbers_str)
        card_total = 0
        for number in my_numbers:
            if number in winning_numbers:
                card_total = card_total * 2 if card_total != 0 else 1
        total += card_total
    print(total)
