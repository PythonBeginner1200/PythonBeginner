def cards_productor():
    cards = []
    color = ['红桃', '黑桃', '方块', '梅花']
    number = list(range(2, 11))
    number.extend(['J', 'Q', 'K', 'A'])
    for i in color:
        for j in number:
            card = (i, j)
            cards.append(card)
    cards.append('JOKER')
    cards.append('joker')
    return cards

if __name__ == '__main__':
    cards = cards_productor()
    for card in cards:
        print(card)
    print('一共{}张牌'.format(len(cards)))