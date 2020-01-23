def number_in_english(num):
    dct = {1: "one", 2: "two",
           3: "three", 4: "four",
           5: "five", 6: 'six',
           7: "seven", 8: "eight",
           9: "nine", 10: "ten",
           11: "eleven", 12: "twelve",
           13: "thirteen", 20: "twenty",
           30: "thirty", 40: "forty",
           50: "fifty", 60: "sixty", 70: "seventy",
           80: "eighty", 90: "ninety",
           0: "", 19: "nineteen",
           18: "eighteen", 17: "seventeen",
           16: "sixteen", 15: "fiveteen",
           14: "fourteen"}
    a, b, c = num // 100, num // 10 % 10 * 10, num % 10
    length = len(str(num))
    if num == 0:
        return "zero"
    if length == 3:
        if int(num % 100) in dct and int(num % 100) != 0:
            return dct[a] + " hundred and " + dct[num % 100]
        if num % 100 <= 20:
            if c == 0 and b == 0:
                return dct[a] + " hundred"
            return dct[a] + " hundred and " + dct[num % 10]
        else:
            return dct[a] + " hundred and " + dct[b] + " " + dct[c]
    elif length == 2:
        if num <= 20:
            return dct[num]
        else:
            if c == 0:
                return dct[b]
            return dct[b] + " " + dct[c]
    else:
        return dct[num]