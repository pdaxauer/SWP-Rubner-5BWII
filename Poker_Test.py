import unittest
from Poker import create_deck, check_Paar, check_Drilling, check_Vierling, check_Flush, check_Strasse


class TestPokerMethods(unittest.TestCase):
    def setUp(self):
        self.farben = ['Herz', 'Karo', 'Pik', 'Kreuz']
        self.werte = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Bube', 'Dame', 'König', 'Sau']
        self.deck = create_deck(self.farben, self.werte)

    def test_check_Paar(self):
        hand = [('2', 'Herz'), ('2', 'Karo'), ('3', 'Pik'), ('4', 'Kreuz'), ('5', 'Herz')]
        self.assertTrue(check_Paar(hand))

    def test_check_Drilling(self):
        hand = [('2', 'Herz'), ('2', 'Karo'), ('2', 'Pik'), ('4', 'Kreuz'), ('5', 'Herz')]
        self.assertTrue(check_Drilling(hand))

    def test_check_Vierling(self):
        hand = [('2', 'Herz'), ('2', 'Karo'), ('2', 'Pik'), ('2', 'Kreuz'), ('5', 'Herz')]
        self.assertTrue(check_Vierling(hand))

    def test_check_Flush(self):
        hand = [('2', 'Herz'), ('3', 'Herz'), ('4', 'Herz'), ('5', 'Herz'), ('6', 'Herz')]
        self.assertTrue(check_Flush(hand))

    def test_check_Strasse(self):
        hand = [('2', 'Herz'), ('3', 'Karo'), ('4', 'Pik'), ('5', 'Kreuz'), ('6', 'Herz')]
        self.assertTrue(check_Strasse(hand, self.werte))


if __name__ == "__main__":
    unittest.main()
