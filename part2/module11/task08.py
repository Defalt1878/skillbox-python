import random
from enum import Enum

print('Задача 8. Блек-джек')


class Suit(Enum):
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4


class CardValue(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 110
    QUEEN = 210
    KING = 310
    ACE = 11


class Card:
    def __init__(self, suit: Suit, value: CardValue):
        self._suit = suit
        self._value = value
        self.score = value.value % 100

    def __str__(self):
        return f'{self._value.name} ({self._suit.name})'


class Deck:
    def __init__(self):
        self.cards = []
        self.new_deck()

    def new_deck(self):
        self.cards.clear()
        for suit in Suit:
            for value in CardValue:
                self.cards.append(Card(suit, value))

    def get_random_card(self):
        return self.cards.pop(random.randint(0, len(self.cards) - 1))


class Player:
    def __init__(self, name: str):
        self.name = name
        self.cards = list[Card]()

    def take_card(self, card: Card):
        self.cards.append(card)

    def get_score(self):
        score = sum([card.score for card in self.cards])
        if score > 21 and 11 in [card.score for card in self.cards]:
            score -= 10
        return score


def player_take_cards(_player: Player, _deck: Deck):
    _player.take_card(_deck.get_random_card())
    _player.take_card(_deck.get_random_card())
    print(f'\nУ вас на руках: {", ".join([str(card) for card in _player.cards])}')
    while True:
        score = _player.get_score()
        print(f'\nОбщий счёт: {score}')
        if score > 21:
            print('У вас перебор! Вы проиграли!')
            break
        if score == 21:
            print('У вас блек-джек!')
            break

        answer = input('Хотите взять ещё карту (да / нет)? ').lower()
        if answer == 'нет':
            break
        if answer != 'да':
            print('Ниче не понял.')
            continue

        card = _deck.get_random_card()
        _player.take_card(card)
        print(f'Вы взяли {card}')


def dealer_take_cards(_dealer: Player, _deck: Deck, _player_score: int):
    _dealer.take_card(_deck.get_random_card())
    _dealer.take_card(_deck.get_random_card())
    print(f'\nКарты на руках у дилера: {", ".join([str(card) for card in _dealer.cards])}')
    while _dealer.get_score() < _player_score:
        card = _deck.get_random_card()
        _dealer.take_card(card)
        print(f'Дилер взял {card}')


deck = Deck()

player = Player('Игрок')
dealer = Player('Дилер')

player_take_cards(player, deck)
player_score = player.get_score()

if player.get_score() > 21:
    quit()

dealer_take_cards(dealer, deck, player_score)
dealer_score = dealer.get_score()

if dealer_score > 21:
    print('У дилера перебор! Вы победили!')
    quit()

print(f'\nВаш счёт: {player_score}')
print(f'Счёт дилера: {dealer_score}')
if player_score > dealer_score:
    print('Вы победили!')
elif player_score < dealer_score:
    print('Вы проиграли!')
else:
    print('Ничья!')
