from treasure_hunt_oo import TreasureHunt

if __name__ == '__main__':
    array = [input().split(" ") for i in range(5)]

    for step in TreasureHunt(array=array):
        print(step, end=" ")
