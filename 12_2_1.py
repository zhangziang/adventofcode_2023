# coding: utf-8
from typing import Tuple

def solution1(red, green, blue :int):
    packet_nums = [red, green, blue]
    result = 0
    with open("12_2.input") as f:  
        for line in f:
            game_no, counts = process_one(line)
            possible = True
            for i in range(3):
                if counts[i] > packet_nums[i]:
                    possible = False
                    break
            if possible:
                result += game_no
    print(f"1 result: {result}")

def solution2():
    result = 0
    with open("12_2.input") as f:  
        for line in f:
            _, counts = process_one(line)
            val = 1
            for count in counts:
                if count != 0:
                    val *= count
            result += val
    print(f"2 result: {result}")
    

def process_one(data: str)-> Tuple[int, list[int]]:
    indexs = {
        "red": 0,
        "green": 1,
        "blue": 2,
    }
    data = data.strip()
    
    temp = data.split(":", 2)
    game_no = int(temp[0][5:])
    plays = temp[1].strip().split(";")
    max_count = [0,0,0] # red, green, blue
    for play in plays:
        cubes = play.split(",")
        for cube in cubes:
            val = cube.strip().split(" ")
            count = int(val[0])
            index = indexs[val[1]]
            max_count[index] = max(max_count[index], count)
    return game_no, max_count

solution1(12, 13, 14)
solution2()
