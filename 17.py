# coding=utf-8
# Number letter counts

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of 'and' when writing out numbers is in compliance with British usage.

from string import ascii_lowercase

literature = {
    0:       'zero',
    1:       'one',
    2:       'two',
    3:       'three',
    4:       'four',
    5:       'five',
    6:       'six',
    7:       'seven',
    8:       'eight',
    9:       'nine',
    10:      'ten',
    11:      'eleven',
    12:      'twelve',
    13:      'thirteen',
    14:      'fourteen',
    15:      'fifteen',
    16:      'sixteen',
    17:      'seventeen',
    18:      'eighteen',
    19:      'nineteen',
    20:      'twenty',
    30:      'thirty',
    40:      'forty',
    50:      'fifty',
    60:      'sixty',
    70:      'seventy',
    80:      'eighty',
    90:      'ninety',
    100:     'hundred',
    1000:    'thousand',
    1000000: 'million'
}

def getLiterature(num):
    result = ''
    if num in literature:
        result = literature[num]

    return result

def splitDigits(num):
    digits = []
    while num > 0:
        digit = num % 10
        digits.append(digit)
        num = num // 10

    return digits

def tens(digits = list()):
    # 1 十位 个位都不是0
    # 2 十位 为0 个位不是0
    # 3 十位 不为0 个位是0
    # 4 数字小于20 直接查表
    result = ''
    if len(digits) >= 2:
        if digits[1] != 0 and digits[0] != 0:
            result = getLiterature(digits[1]*10) + '-' + getLiterature(digits[0])
        if digits[1] == 0 and digits[0] != 0:
            result = getLiterature(digits[0])
        if digits[1] != 0 and digits[0] == 0:
            result = getLiterature(digits[1]*10)

    return result

def hundreds(digits = list()):
    # 1 百位为 0
    # 2 百位不为 0
    result = ''
    if len(digits) >= 3 and digits[2] != 0:
        result = getLiterature(digits[2]) + ' ' + getLiterature(100)

    return result

def thousands(digits = list()):
    # 千位为 0
    # 千位不为 0
    result = ''
    if len(digits) >= 4 and digits[3] != 0:
        result = getLiterature(digits[3]) + ' ' + getLiterature(1000)

    return result

# 0-20 查字典
# 20以上 拆分数字的方法
def translate(num):
    result = ''
    digits       = splitDigits(num)
    digits_len   = len(digits)
    res_ten      = tens(digits)
    res_hundred  = hundreds(digits)
    res_thousand = thousands(digits)

    num_tens = num % 100
    if num_tens > 0 and num_tens <= 20:
        res_ten = getLiterature(num_tens)

    # 1 都是 '' 那么就是'' 
    # 2 只有res_ten 就是res_ten
    # 3 只有res_hundred 就是 res_hundred
    # 4 只有res_thousand 就是 res_thousand
    # 5 res_ten 和 res_hundred 110 => one hundred and ten
    # 6 res_ten and res_thousand 1011 => one thousand and eleven
    # 7 res_hundred and res_thousand 1200 => one thousand and two hundred
    # 8 res_ten and res_hundred and res_thousand 1234 => one thousand two hundred and thirty-four
    
    if       res_ten and not res_hundred and not res_thousand:
        result = res_ten
    elif not res_ten and     res_hundred and not res_thousand:
        result = res_hundred
    elif not res_ten and not res_hundred and     res_thousand:
        result = res_thousand
    elif     res_ten and     res_hundred and not res_thousand:
        result = res_hundred + ' and ' + res_ten
    elif     res_ten and not res_hundred and     res_thousand:
        result = res_thousand + ' and ' + res_ten
    elif not res_ten and     res_hundred and     res_thousand:
        result = res_thousand + ' and ' + res_hundred
    elif     res_ten and     res_hundred and     res_thousand:
        result = res_thousand + ' ' + res_hundred + ' and ' + res_ten

    return result

def countLetters(string):
    result = 0
    for i in string:
        if i in ascii_lowercase:
            result += 1

    return result

def solve(max_num):
    alphaSum = 0
    f = open('number-literature', 'w')
    for i in range(1, max_num+1):
        result = translate(i)
        alphaSum += countLetters(result)
        f.write(result + " ")
        f.write(str(countLetters(result)))
        f.write('\n')
        # print(result, countLetters(result))

    # print(alphaSum)
    f.write(str(alphaSum))
    f.flush()
    f.close()

solve(1000)

# 遍地都是坑啊
# (0, 20] 要特殊处理
# 1000 不能翻译成one thousand and zero
# 分八种情况讨论也是醉了.....
# 
