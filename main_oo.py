from treasure_hunt_oo import TreasureHuntOO

if __name__ == '__main__':
    array = [input().split(" ") for i in range(5)]

    for step in TreasureHuntOO(array=array):
        print(step, end=" ")
