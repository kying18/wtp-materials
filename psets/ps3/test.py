import unittest

from blackjack import blackjack_solution
from translator import numbers_translation
from simple_graphics import *


def blackjack(card1, card2, dealer_card):
    total = card1 + card2
    if total == 21:
        return "blackjack!"
    elif total > 17:
        return "stand"
    elif total > 12:
        if dealer_card > 6:
            return "hit"
        else:
            return "stand"
    elif total > 9 or (total == 9 and dealer_card < 6):
        return "double, then hit"
    else:
        return "hit"


class TestBlackjack(unittest.TestCase):
    def test_blackjack_row_1(self):
        cards, action = blackjack_solution.items()[0]
        self.assertEqual(blackjack(*cards), action)

    def test_blackjack_row_2(self):
        cards, action = blackjack_solution.items()[1]
        self.assertEqual(blackjack(*cards), action)

    def test_blackjack_row_3(self):
        cards, action = blackjack_solution.items()[2]
        self.assertEqual(blackjack(*cards), action)

    def test_blackjack_row_4(self):
        cards, action = blackjack_solution.items()[3]
        self.assertEqual(blackjack(*cards), action)

    def test_blackjack_row_5(self):
        cards, action = blackjack_solution.items()[4]
        self.assertEqual(blackjack(*cards), action)


class TestTranslation(unittest.TestCase):
    # cero uno dos tres cuatro cinco seis siete ocho nueve
    def test_spanish_translate_0(self):
        self.assertEqual(numbers_translation["zero"], "cero", '"zero" should map to "cero"')

    def test_spanish_translate_1(self):
        self.assertEqual(numbers_translation["one"], "uno", '"one" should map to "uno"')

    def test_spanish_translate_2(self):
        self.assertEqual(numbers_translation["two"], "dos", '"two" should map to "dos"')

    def test_spanish_translate_3(self):
        self.assertEqual(numbers_translation["three"], "tres", '"three" should map to "tres"')

    def test_spanish_translate_4(self):
        self.assertEqual(numbers_translation["four"], "cuatro", '"four" should map to "cuatro"')

    def test_spanish_translate_5(self):
        self.assertEqual(numbers_translation["five"], "cinco", '"five" should map to "cinco"')

    def test_spanish_translate_6(self):
        self.assertEqual(numbers_translation["six"], "seis", '"six" should map to "seis"')

    def test_spanish_translate_7(self):
        self.assertEqual(numbers_translation["seven"], "siete", '"seven" should map to "siete"')

    def test_spanish_translate_8(self):
        self.assertEqual(numbers_translation["eight"], "ocho", '"eight" should map to "ocho"')

    def test_spanish_translate_9(self):
        self.assertEqual(numbers_translation["nine"], "nueve", '"nine" should map to "nueve"')


class TestSimpleGraphics(unittest.TestCase):
    def test_double_radius(self):
        self.assertEqual(c.getRadius(), 20, "Radius should be double the original")

    def test_upper_right(self):
        center_point = c.getCenter()
        self.assertGreater(center_point.getX(), 50, "Circle center should be on the right side")
        self.assertLess(center_point.getY(), 50, "Circle center should be on the top half")

    def test_yellow_fill(self):
        self.assertEqual(c.getFill(), "yellow", "Circle fill should be yellow")

    def test_purple_outline(self):
        self.assertEqual(c.getOutline(), "purple", "Circle outline should be purple")


if __name__ == "__main__":
    unittest.main()
