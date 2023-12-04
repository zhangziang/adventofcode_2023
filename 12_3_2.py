# coding: utf-8

def solution2():
    num_list,sysmbol_map, x, y = process_data("12_3.input")
    # check num is useful
    match_sysmbol = {}
    for item in num_list:
        num = item[0]
        num_local = item[1:]
        y_start = max(num_local[0]-1,0)
        y_end = min(num_local[0]+1, y)
        x_start = max(num_local[1]-1, 0)
        x_end = min(num_local[2]+1, x)
        hit = False
        for i in range(x_start, x_end+1):
            for j in range(y_start, y_end+1):
                if (j,i) in sysmbol_map:
                    hit= True
                    if (j,i) in match_sysmbol:
                        match_sysmbol[(j,i)].append(num)
                    else:            
                        match_sysmbol[(j,i)]= [num]
                    break
            if hit:
                break
    result = 0
    for num_list in match_sysmbol.values():
        if len(num_list) == 1:
            continue
        if len(num_list) == 2:
            result += num_list[0] * num_list[1]
        else:
            print("meet some wrong data")
    print("---result---")
    print(result)

def process_data(filename: str) -> list[str]:
    num_list = [] # num, localtion (y,x1,x2)
    sysmbol_map = {} # localtion -> bool 
    num_ing = False
    num_str = ""
    num_x_1 = 0
    num_x_2 = 0
    x = -1
    with open(filename) as r:
        y = -1
        for line in r:
            y += 1
            x = -1
            for i in line.strip():
                x += 1   
                if i >='0' and i<= '9':
                    if not num_ing:
                        num_x_1 = x
                        num_x_2 = x
                        num_ing = True
                    else:
                        num_x_2 = x
                    num_str += i
                else:
                    if num_ing:
                        num_ing = False
                        _num = int(num_str)
                        num_str = ""
                        num_list.append((_num, y, num_x_1, num_x_2))
                    if i == "*":
                        sysmbol_map[(y,x)] = True
            # 循环结束，判断是否还有没有处理的 num
            if num_ing:
                num_ing = False
                _num = int(num_str)
                num_str = ""
                num_list.append((_num, y, num_x_1, num_x_2))
    return num_list, sysmbol_map, x, y

solution2()