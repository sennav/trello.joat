import os
import json
import math

END = '\033[0m'
BOLD = '\033[1m'
RED = '\033[91m'
BLUE = '\033[36m'


def get_text_bold(text):
    return f'{BOLD}{text}{END}'


def get_header(lists, icw, separator):
    header = ''
    for single_list in lists:
        if single_list != lists[-1]:
            header += f"{single_list.get('name'):^{icw}.{icw}}{separator}"
        else:
            header += f"{single_list.get('name'):^{icw}.{icw}}"
    return get_text_bold(header)


def get_cards_lists(lists, cards):
    cards_lists = []
    for single_list in lists:
        list_id = single_list.get('id')
        list_cards = [card for card in cards if card['idList'] == list_id]
        cards_lists.append(list_cards)
    return cards_lists


def get_card_number(card):
    truncated_number = str(card.get('idShort'))[-4:]
    return f'{truncated_number} '


def get_card_cell(card_list, row_number, icw, separator, last):
    try:
        card = card_list[row_number]
        sep = separator
        if last:
            sep = ''
        card_number = get_card_number(card)
        name_width = icw - len(card_number)
        bold_card_bumber = get_text_bold(card_number)
        return f"{bold_card_bumber}{card.get('name'):{name_width}.{name_width}}{sep}"
    except IndexError:
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
print('‾' * terminal_width)
print(header)
print('_' * terminal_width)
for row in cards_rows:
    print(row)
