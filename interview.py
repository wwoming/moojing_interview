

def how_many_ways(digitarray):
    length = len(digitarray)
    # 当序列长度等于1或者长度为2并且第一位为0时，只有一种结果
    if length < 2 or (int(digitarray[0] == 0) and length == 2):
        return 1
    else:
        num = 1
        a = 0
        # 当序列长度大于2并且第一位为0时，要从第2位开始组合
        if int(digitarray[0]) == 0 and length > 2:
            a = 1
        for n in range(a, length-1):
            i = int(digitarray[n])
            j = int(digitarray[n+1])
            if (i == 1 and 0 <= j <= 9) or (i == 2 and 0 <= j <= 6):
                num += 1
        return num





