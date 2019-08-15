import os
import json
import math


def get_header(lists, icw, separator):
    header = ''
    for single_list in lists:
        if single_list != lists[-1]:
            header += f"{single_list.get('name'):^{icw}.{icw}}{separator}"
        else:
            header += f"{single_list.get('name'):^{icw}.{icw}}"
    return header


def get_cards_lists(lists, cards):
    cards_lists = []
    for single_list in lists:
        list_id = single_list.get('id')
        list_cards = [card for card in cards if card['idList'] == list_id]
        cards_lists.append(list_cards)
    return cards_lists


def get_card_cell(card_list, row_number, icw, separator, last):
    try:
        card = card_list[row_number]
        if last:
            return f"{card.get('name'):{icw}.{icw}}"
        else:
            return f"{card.get('name'):{icw}.{icw}}{separator}"
    except Exception:
        if last:
            return f"{' ':^{icw}.{icw}}"
        else:
            return f"{' ':^{icw}.{icw}}{separator}"


def get_cards_rows(cards_lists, icw, separator):
    no_rows = max(len(c_list) for c_list in cards_lists)
    rows = []
    for row_number in range(0, no_rows):
        row_str = ''
        for card_list in cards_lists:
            last = card_list == cards_lists[-1]
            cell = get_card_cell(card_list, row_number, icw, separator, last)
            row_str += cell
        rows.append(row_str)
    return rows


lists = json.loads(os.getenv('LISTS'))
cards = json.loads(os.getenv('CARDS'))

terminal_width = int(os.getenv('WIDTH'))
separator = ' | '
width_without_separators = terminal_width - ((len(lists) - 1) * len(separator))
icw = math.floor(width_without_separators / len(lists))

header = get_header(lists, icw, separator)
cards_lists = get_cards_lists(lists, cards)
cards_rows = get_cards_rows(cards_lists, icw, separator)
print(header)
print('-' * terminal_width)
for row in cards_rows:
    print(row)
