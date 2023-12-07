from collections import Counter
from functools import cmp_to_key

CARD_SCORES = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10} | {str(x): x for x in range(2, 10)}
JOKER_MODE = False


def solve(hands_ranks, joker_mode=False) -> int:
    global JOKER_MODE
    JOKER_MODE = joker_mode
    if JOKER_MODE:
        CARD_SCORES["J"] = 1
    sorted_hands = sorted(list(hands_ranks.keys()), key=cmp_to_key(compare_hands))
    return sum((i + 1) * hands_ranks[card] for i, card in enumerate(sorted_hands))


def compare_hands(hand1, hand2):
    if calculate_hand_strength(hand1) < calculate_hand_strength(hand2):
        return -1
    elif calculate_hand_strength(hand1) > calculate_hand_strength(hand2):
        return 1
    else:
        return compare_card_strength(hand1, hand2)


def calculate_hand_strength(hand):
    hand_counter = Counter(hand)
    if JOKER_MODE and 'J' in hand:
        hand_counter = convert_joker(hand_counter)
    # five of a kind
    if len(hand_counter) == 1:
        return 7
    # four of a kind
    elif 4 in hand_counter.values():
        return 6
    # full house
    elif len(hand_counter.values()) == 2:
        return 5
    # three of a kind
    elif 3 in hand_counter.values():
        return 4
    # two pair
    elif len(hand_counter.values()) == 3:
        return 3
    # one pair
    elif 2 in hand_counter.values():
        return 2
    # high card
    return 1


def convert_joker(hand_counter):
    num_jokers = hand_counter["J"]
    if hand_counter["J"] == 5:
        return Counter("AAAAA")
    hand_counter.pop("J")
    most_keys = [k for k, v in hand_counter.items() if v == max(hand_counter.values())]
    card_to_increment = most_keys[0] if len(most_keys) == 1 else max(hand_counter.keys(), key=lambda x: CARD_SCORES[x])
    hand_counter[card_to_increment] += num_jokers
    return hand_counter


def compare_card_strength(card1, card2):
    for pair in zip(card1, card2):
        card_1 = CARD_SCORES[pair[0]]
        card_2 = CARD_SCORES[pair[1]]
        if card_1 > card_2:
            return 1
        elif card_1 < card_2:
            return -1
    return 0
