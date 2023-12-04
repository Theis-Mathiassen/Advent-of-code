import re

with open('4/input.txt') as f:
    lines = f.readlines()
    total = 0
    number_of_cards = [1]*len(lines)
    for i, line in enumerate(lines):
        card, numbers = line.split(":")
        card_number = int(re.findall(r'\d+', card)[0])
        my_numbers_str, winning_numbers_str = numbers.split('|')
        my_numbers = re.findall(r'\d+', my_numbers_str)
        winning_numbers = re.findall(r'\d+', winning_numbers_str)
        card_winning_numbers = 0

        for number in my_numbers:
            if number in winning_numbers:
                card_winning_numbers += 1# card_total * 2 if card_total != 0 else 1
        for j in range(card_winning_numbers):
            number_of_cards[min(i+j+1,len(number_of_cards)-1)] += number_of_cards[i]
    
    for cards in number_of_cards:
        total += cards
    print(total)
