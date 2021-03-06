from exceptions import NoTreasureFoundException
from treasure_hunt_functional import treasure_hunt_with_lambda

if __name__ == '__main__':
    array = [input().split(" ") for i in range(5)]
    try:
        for step in treasure_hunt_with_lambda(array=array):
            print(step, end=" ")
    except NoTreasureFoundException:
        print("NO TREASURE")
