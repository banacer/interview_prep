
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
def compute_valid_ip(s,num):
    if num < 1 and not s:
        return ['']
    elif num < 1:
        return None

    i = 1
    l = []
    while int(s[:i]) < 256 and i < len(s):
        sub_l = compute_valid_ip(s[i:], num - 1)
        if not sub_l:
            continue
        for word in sub_l:
            if not word:
                continue
            r = s[:i] + '.'+ word
            print r
            l.append(r)
        i += 1
        print 'hey',s[:i], s
    return l
def str_encode(s):
    char = s[0]
    count = 1
    encoded = ''
    for c in s[1:]:
        if c != char:
            encoded += str(count)+char
            char = c
            count = 1
        else:
            count+=1
    encoded += str(count) + char
    return encoded
def str_decode(s):
    decoded = ''
    for n,c in [(int(s[i]),s[i+1]) for i in range(0,len(s),2)]:
        decoded += c*n
    return decoded
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
    assert set(compute_mnemonics('22')) == set(['AA', 'AB', 'AC', 'BA', 'BB', 'BC', 'CA', 'CB', 'CC'])
    #print compute_valid_ip('19216811',4)
    assert str_encode('aaabbccccdee') == '3a2b4c1d2e'
    assert str_decode('3a2b4c1d2e') == 'aaabbccccdee'