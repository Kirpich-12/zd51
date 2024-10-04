from math import factorial as fac
input_data = open('input.txt', 'r')
data_s = input_data.read()
data = data_s.split()

ans = 1
ch = int(data[0])
fact = data(data[1])

if fact == '!':
    ans = str(fac(ch))
elif fact == '!!':
    k = 2
    if ch // k == 0:
        for i in range(1, ch + 1):
            for j in range(ch):
                ans *= i - j
            
