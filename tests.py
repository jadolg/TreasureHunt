import unittest

from exceptions import NoTreasureFoundException
from treasure_hunt_functional import get_cell
from treasure_hunt_oo import TreasureHuntOO

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
        treasure_hunt_oo = TreasureHuntOO(array=INPUT)
        self.assertEqual(OUTPUT, list(treasure_hunt_oo), "Output did not match the expected values")

    def test_hunt_no_treasure(self):
        with self.assertRaises(NoTreasureFoundException):
            list(TreasureHuntOO(array=INPUT_NO_TREASURE))
