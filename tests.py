import unittest

from exceptions import NoTreasureFoundException
from treasure_hunt_functional import get_cell, treasure_hunt_with_lambda, treasure_hunt_with_closure
from treasure_hunt_oo import TreasureHunt

INPUT = [
    ["55", "14", "25", "52", "21"],
    ["44", "31", "11", "53", "43"],
    ["24", "13", "45", "12", "34"],
    ["42", "22", "43", "32", "41"],
    ["51", "23", "33", "54", "15"]
]

# Cells 11 and 22 are in loop
# If I detect a loop before finding a result it means there is no treasure
INPUT_NO_TREASURE = [
    ["22", "14", "25", "52", "21"],
    ["44", "11", "11", "53", "43"],
    ["24", "13", "45", "12", "34"],
    ["42", "22", "43", "32", "41"],
    ["51", "23", "33", "54", "15"]
]

OUTPUT = ["11", "55", "15", "21", "44", "32", "13", "25", "43"]


class TreasureHuntOOTestCase(unittest.TestCase):
    def test_hunt(self):
        treasure_hunt_oo = TreasureHunt(array=INPUT)
        self.assertEqual(OUTPUT, list(treasure_hunt_oo), "Output did not match the expected values")

    def test_hunt_no_treasure(self):
        with self.assertRaises(NoTreasureFoundException):
            list(TreasureHunt(array=INPUT_NO_TREASURE))


class TreasureHuntFunctionalTestCase(unittest.TestCase):
    def test_get_cell(self):
        self.assertEqual(INPUT[0][0], get_cell("11", array=INPUT))

    def test_hunt_with_lambda(self):
        self.assertEqual(OUTPUT, treasure_hunt_with_lambda(array=INPUT))

    def test_hunt_no_treasure_with_lambda(self):
        with self.assertRaises(NoTreasureFoundException):
            treasure_hunt_with_lambda(array=INPUT_NO_TREASURE)

    def test_hunt_with_closure(self):
        self.assertEqual(OUTPUT, treasure_hunt_with_closure(array=INPUT))

    def test_hunt_no_treasure_with_closure(self):
        with self.assertRaises(NoTreasureFoundException):
            treasure_hunt_with_closure(array=INPUT_NO_TREASURE)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
