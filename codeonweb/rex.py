import re

s = '100 NORTH BROAD ROAD'
print(re.sub('ROAD$', 'RD.', s))


s = '100 BROAD'
print(re.sub('ROAD$', 'RD.', s))
print(re.sub('\\bROAD$', 'RD.', s))
print(re.sub(r'\bROAD$', 'RD.', s))
s = '100 BROAD ROAD APT. 3'
print(re.sub(r'\bROAD$', 'RD.', s))
print(re.sub(r'\bROAD\b', 'RD.', s))


pattern = '^M?M?M?$'
print(re.search(pattern, 'M'))
print(re.search(pattern, 'MMM MMM'))

pattern = '^M{0,3}$'
print(re.search(pattern, 'MMM'))

pattern = '''
    ^                   # 문자열의 시작
    M{0,3}              # 천의 자리 - 0-3 개의 M
    (CM|CD|D?C{0,3})    # 백의 자리 - 900(CM), 400(CD), 0-300(0-3 개의 C),
                        #           500-800(D 하나와, 뒤이은 0 to 3 개의 C)
    (XC|XL|L?X{0,3})    # 십의 자리 - 90(XC), 40(XL), 0-30(0-3 개의 X),
                        #           50-80(L 하나와, 뒤이은 0-3 개의 X)
    (IX|IV|V?I{0,3})    # 일의 자리 - 9(IX), 4(IV), 0-3(0-3 개의 I),
                        #           5-8(V 하나와 뒤이은 0-3 개의 I)
    $                   # 문자열의 끝
    '''
print(re.search(pattern, 'M', re.VERBOSE))


phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')
print(phonePattern.search('800-555-1212').groups())
#print(phonePattern.search('800-555-1212-1234'))
#print(phonePattern.search('800-555-1212-1234').groups())

phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})-(\d+)$')
print(phonePattern.search('800-555-1212-1234').groups())
print(phonePattern.search('800 555 1212 1234'))
print(phonePattern.search('800-555-1212'))


phonePattern = re.compile(r'^(\d{3})\D+(\d{3})\D+(\d{4})\D+(\d+)$')
print(phonePattern.search('800 555 1212 1234').groups())
print(phonePattern.search('800-555-1212-1234').groups())
print(phonePattern.search('80055512121234'))
print(phonePattern.search('800-555-1212'))

phonePattern = re.compile(r'^(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
print(phonePattern.search('80055512121234').groups())
print(phonePattern.search('800.555.1212 x1234').groups())
print(phonePattern.search('800-555-1212').groups())
print(phonePattern.search('(800)5551212 x1234'))

phonePattern = re.compile(r'^\D*(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
print(phonePattern.search('(800)5551212 ext. 1234').groups())
print(phonePattern.search('800-555-1212').groups())
print(phonePattern.search('work 1-(800) 555.1212 #1234'))

phonePattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
print(phonePattern.search('work 1-(800) 555.1212 #1234').groups())
print(phonePattern.search('800-555-1212').groups())
print(phonePattern.search('80055512121234').groups())