
def decode(s):
    if not s:
        return 0
    negative = False
    if s[0] == '-':
        negative = True
        s = s[1:]
    number = 0
    for c in s:
        number*=10
        number+= ord(c)-ord('0')
    if negative:
        return number*-1
    return number

def base_convert(s, b1, b2):
    if not s:
        return 0
    negative = False
    if s[0] == '-':
        negative = True
        s = s[1:]
    number = 0
    for c in s:
        number*=b1
        number+= ord(c)-ord('0')
    n1 = ""
    k = 0
    while number > 0:
        d = number % b2
        n1 = to_hex(d) + n1
        number /=b2
    if negative:
        return '-'+n1
    return n1

def to_hex(n):
    if n < 10:
        return str(n)
    elif n == 10:
        return 'A'
    elif n == 11:
        return 'B'
    elif n == 12:
        return 'C'
    elif n == 13:
        return 'D'
    elif n == 14:
        return 'E'
    elif n == 15:
        return 'F'
def convert_spreadsheet_col(s):
    n = 0
    for c in s:
        n*=26
        n+= ord(c)-ord('A')+1
    return n

def test_palindromicity(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if not s[i].isalpha():
            i+=1
            continue
        if not s[j].isalpha():
            j-=1
            continue
        if s[i].lower() != s[j].lower():
            return False
        i+=1
        j-=1
    return True

def compute_mnemonics(n):
    mnem = ['','','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
    if not n:
        return ['']
    i = ord(n[0]) - ord('0')
    l = []
    for c in mnem[i]:
        l_temp = compute_mnemonics(n[1:])
        for w in l_temp:
            l.append(c+w)
    return l

if __name__ == '__main__':
    assert decode('123') == 123
    assert decode('-025') == -25
    assert decode('-0') == 0
    assert base_convert('122',10,16) == '7A'
    assert base_convert('578', 10, 16) == '242'
    assert convert_spreadsheet_col('AA') == 27
    assert convert_spreadsheet_col('ZZ') == 702
    assert test_palindromicity('Ray a Ray') == False
    assert test_palindromicity('a man, a plan, a canal, Panama') == True
    print compute_mnemonics('22')