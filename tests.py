import unittest

from treasure_hunt_oo import TreasureHuntOO

INPUT = [
    ["55", "14", "25", "52", "21"],
    ["44", "31", "11", "53", "43"],
    ["24", "13", "45", "12", "34"],
    ["42", "22", "43", "32", "41"],
    ["51", "23", "33", "54", "15"]
]

OUTPUT = ["11", "55", "15", "21", "44", "32", "13", "25", "43"]


class TreasureHuntOOTestCase(unittest.TestCase):
    def test_hunt(self):
        treasure_hunt = TreasureHuntOO(array=INPUT)
        self.assertEqual(OUTPUT, list(treasure_hunt), "Output did not match the expected values")
