from main import calculate
import unittest

usb_size = 1
memes = [
    ('rollsafe.jpg', 205, 6),
    ('sad_pepe_compilation.gif', 410, 10),
    ('yodeling_kid.avi', 605, 12)
]

usb_size2 = 64
memes2 = [
    ('a', 204, 70,),
    ('b', 22400, 800),
    ('c', 234, 80),
    ('d', 5000, 240),
    ('e', 64000, 6700),
    ('f', 32000, 5400),
    ('g', 32000, 5300)
]

usb_size3 = 1
memes3 = [
    ('a', 140, 5),
    ('b', 33, 62),
    ('c', 100, 4),
    ('d', 230, 16),
    ('e', 340, 3),
    ('f', 900, 17)
]

usb_size4 = 2
memes4 = [
    ('a', 10, 45),
    ('b', 50, 16),
    ('c', 99, 28),
    ('d', 130, 42),
    ('e', 189, 311),
    ('f', 1664, 1119)
]


class TestKnapsack(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(calculate(usb_size, memes),
                         (22, {'yodeling_kid.avi', 'sad_pepe_compilation.gif'}))

    def test_harder(self):
        self.assertEqual(calculate(usb_size2, memes2),
                         (10850, {'a', 'c', 'f', 'g'}))

    def test_harder2(self):
        self.assertEqual(calculate(usb_size3, memes3),
                         (90, {'a', 'd', 'e', 'c', 'b'}))

    def test_harder3(self):
        self.assertEqual(calculate(usb_size4, memes4),
                         (1533, {'b', 'e', 'a', 'f', 'd'}))


unittest.main()
