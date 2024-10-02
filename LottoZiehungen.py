import random


def ziehung():
    zahlen = list(range(1, 46))
    lotto_zahlen = []

    for index in range(6):
        index = random.randint(0, len(zahlen) - 1)
        lotto_zahlen.append(zahlen[index])
        zahlen[index], zahlen[-1] = zahlen[-1], zahlen[index]
        zahlen = zahlen[:-1]

    return lotto_zahlen


def statistik():
    statistik_dict: dict = {i: 0 for i in range(1, 46)}
    for _ in range(1000):
        lotto_zahlen = ziehung()
        for zahl in lotto_zahlen:
            statistik_dict[zahl] += 1

    return statistik_dict


def main():
    print("Gezogene Zahlen:", ziehung())
    statistik_auswertung = statistik()
    print("\nStatistik nach 1000 Ziehungen:")
    for zahl, haeufigkeit in statistik_auswertung.items():
        print(f"Zahl {zahl}: {haeufigkeit} mal gezogen")
        

if __name__ == "__main__":
    main()
