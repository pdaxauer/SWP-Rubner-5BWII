import random
from collections import Counter

Farbe = ['Herz', 'Karo', 'Pik', 'Kreuz']
Wert = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Bube', 'Dame', 'König', 'Sau']

deck = [(w, f) for w in Wert for f in Farbe]


def draw_hand():
    return random.sample(deck, 5)


hand = draw_hand()


def check_Paar(hand):
    value_counts = Counter([card[0] for card in hand])
    for count in value_counts.values():
        if count == 2:
            return True

    return False


def check_Drilling(hand):
    value_counts = Counter([card[0] for card in hand])
    for count in value_counts.values():
        if count == 3:
            return True

    return False


def check_Vierling(hand):
    value_counts = Counter([card[0] for card in hand])
    for count in value_counts.values():
        if count == 4:
            return True

    return False


def check_Flush(hand):
    value_counts = Counter([card[0] for card in hand])
    for count in value_counts.values():
        if count == 5:
            return True

    return False


def check_FullHouse(hand):
    value_counts = Counter([card[0] for card in hand])
    has_three = False
    has_two = False
    for count in value_counts.values():
        if count == 3:
            has_three = True
        elif count == 2:
            has_two = True
    return has_three and has_two


def check_Strasse(hand):
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Bube', 'Dame', 'König', 'Sau']
    value_indices = sorted([values.index(card[0]) for card in hand])

    for i in range(4):
        if value_indices[i + 1] != value_indices[i] + 1:
            return False
    return True



def check_StraightFlush(hand):
    return check_Strasse(hand) and check_Flush(hand)


def check_RoyalFlush(hand):
    values = ['10', 'Bube', 'Dame', 'König', 'Sau']
    suits = [card[1] for card in hand]
    return all(card[0] in values for card in hand) and len(set(suits)) == 1


def simulate_poker(n=100000):
    results = {
        "Pair": 0,
        "Drilling": 0,
        "Full House": 0,
        "Strasse": 0,
        "Flush": 0,
        "Vierling": 0,
        "Straight Flush": 0,
        "Royal Flush": 0
    }

    for _ in range(n):
        hand = draw_hand()

        if check_Paar(hand):
            results["Pair"] += 1
        if check_Drilling(hand):
            results["Drilling"] += 1
        if check_FullHouse(hand):
            results["Full House"] += 1
        if check_Strasse(hand):
            results["Strasse"] += 1
        if check_Flush(hand):
            results["Flush"] += 1
        if check_Vierling(hand):
            results["Vierling"] += 1
        if check_StraightFlush(hand):
            results["Straight Flush"] += 1
        if check_RoyalFlush(hand):
            results["Royal Flush"] += 1

    for combination in results:
        results[combination] = (results[combination] / n) * 100

    return results


results = simulate_poker(100000)
for combination, percentage in results.items():
    print(f"{combination}: {percentage:.2f}%")
