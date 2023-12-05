# coding: utf-8

import math

def solution1():
    result = 0
    with open("12_4.input") as f:
        for line in f:
            cards = line.strip().split(":")[1].split("|")
            win_nums = set(map(lambda x: int(x),cards[0].split()))
            my_nums = set(map(lambda x: int(x),cards[1].split()))
            hit = win_nums & my_nums
            if len(hit) == 0:
                continue
            result +=  int(math.pow(2, (len(hit) - 1)))
    print(f"result:{result}")

def solution2():
    card_nums = {}
    with open("12_4.input") as f:
        line_num = 0
        for line in f:
            line_num += 1
            cards = line.strip().split(":")[1].split("|")
            win_nums = set(map(lambda x: int(x),cards[0].split()))
            my_nums = set(map(lambda x: int(x),cards[1].split()))
            hit = win_nums & my_nums
            if len(hit) == 0:
                if line_num in card_nums:
                    card_nums[line_num] += 1
                else:
                    card_nums[line_num] = 1
            else:
                if line_num in card_nums:
                    base = card_nums[line_num] + 1
                    card_nums[line_num] += 1
                else:
                    base = 1
                    card_nums[line_num] = 1
                for i in range(line_num+1, line_num+len(hit)+1):
                    if i in card_nums:
                        card_nums[i] += base
                    else:
                        card_nums[i] = base
    result = 0
    for i in range(1, line_num+1):
        result += card_nums[i]
    print(f"result:{result}")

solution2()
