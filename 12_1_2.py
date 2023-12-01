# coding: utf-8

def process_all():
    with open("2.input") as f:
        vals = []
        for line in f:
            val = process_one(line)
            print(line.strip(), val)
            vals.append(val)
        print("---over---")
        print(sum(vals))

def process_one(t: str)-> int:
    # from left to right parse
    t = t.strip()
    result = ""
    lenght = len(t)
    index = -1
    for i in t:
        index += 1
        if i >= "1" and i<="9":
            result += i
        if lenght - index <= 2:
            continue
        match t[index:index+2]:
            case "on": #one
                if t[index:index+3] == "one":
                    result += "1"
            case "tw": #two
                if t[index:index+3] == "two":
                    result += "2"
            case "th": #three
                if t[index:index+5] == "three":
                    result += "3"
            case "fo": #four
                if t[index:index+4] == "four":
                    result += "4"
            case "fi": #five
                if t[index:index+4] == "five":
                    result += "5"
            case "si": #six
                if t[index:index+3] == "six":
                    result += "6"
            case "se": #seven
                if t[index:index+5] == "seven":
                    result += "7"
            case "ei": #eight
                if t[index:index+5] == "eight":
                    result += "8"
            case "ni": #nine
                if t[index:index+4] == "nine":
                    result += "9"                
    if len(result) == 0:
        print("result is empty")
        exit(-1)
    if len(result) == 1:
        return int(result) * 10 + int(result)
    return int(result[0])*10 + int(result[-1])


process_all()