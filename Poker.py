import random
from collections import Counter


def create_deck(farben, werte):
    return [(w, f) for w in werte for f in farben]


def draw_hand(deck):
    return random.sample(deck, 5)


def check_Paar(hand):
    value_counts = Counter([card[0] for card in hand])
    return any(count == 2 for count in value_counts.values())


def check_Drilling(hand):
    value_counts = Counter([card[0] for card in hand])
    return any(count == 3 for count in value_counts.values())


def check_Vierling(hand):
    value_counts = Counter([card[0] for card in hand])
    return any(count == 4 for count in value_counts.values())


def check_Flush(hand):
    suits = [card[1] for card in hand]
    return len(set(suits)) == 1


def check_FullHouse(hand):
    value_counts = Counter([card[0] for card in hand])
    has_three = 3 in value_counts.values()
    has_two = 2 in value_counts.values()
    return has_three and has_two


def check_Strasse(hand, werte):
    value_indices = sorted([werte.index(card[0]) for card in hand])
    return all(value_indices[i + 1] == value_indices[i] + 1 for i in range(4))


def check_StraightFlush(hand, werte):
    return check_Strasse(hand, werte) and check_Flush(hand)


def check_RoyalFlush(hand, werte):
    royal_values = werte[-5:]
    suits = [card[1] for card in hand]
    return all(card[0] in royal_values for card in hand) and len(set(suits)) == 1


def simulate_poker(deck, werte, n):
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
        hand = draw_hand(deck)
        if check_Paar(hand):
            results["Pair"] += 1
        if check_Drilling(hand):
            results["Drilling"] += 1
        if check_FullHouse(hand):
            results["Full House"] += 1
        if check_Strasse(hand, werte):
            results["Strasse"] += 1
        if check_Flush(hand):
            results["Flush"] += 1
        if check_Vierling(hand):
            results["Vierling"] += 1
        if check_StraightFlush(hand, werte):
            results["Straight Flush"] += 1
        if check_RoyalFlush(hand, werte):
            results["Royal Flush"] += 1

    for combination in results:
        results[combination] = (results[combination] / n) * 100

    return results


def main():
    farben = ['Herz', 'Karo', 'Pik', 'Kreuz']
    werte = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Bube', 'Dame', 'König', 'Sau']
    deck = create_deck(farben, werte)

    n = int(input("Anzahl der Simulationen eingeben: "))

    results = simulate_poker(deck, werte, n)
    for combination, percentage in results.items():
        print(f"{combination}: {percentage:.2f}%")


if __name__ == "__main__":
    main()
