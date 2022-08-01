# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.

input_str = '2+2*2+(1*1)'
str = list(input_str)
def transformation(str):
    new_digit = []
    for i in range(len(str)):
        if str[i].isdigit() == 1:
            new_digit.append(int(str[i]))
        else:
            new_digit.append(str[i])
    return new_digit
new_digit = transformation(str)
print(new_digit)

def mult(new_digit):
    i = new_digit.index('*')
    res = new_digit[i-1]*new_digit[i+1]
    new_digit[i-1] = res
    new_digit.pop(i+1)
    new_digit.pop(i)
    return res
def div(new_digit):
    i = new_digit.index('/')
    res = new_digit[i-1]/new_digit[i+1]
    new_digit[i-1] = res
    new_digit.pop(i+1)
    new_digit.pop(i)
    return res
def sum(new_digit):
    i = new_digit.index('+')
    res = new_digit[i-1]+new_digit[i+1]
    new_digit[i-1] = res
    new_digit.pop(i+1)
    new_digit.pop(i)
    return res
def diff(new_digit):
    i = new_digit.index('-')
    res = new_digit[i-1]-new_digit[i+1]
    new_digit[i-1] = res
    new_digit.pop(i+1)
    new_digit.pop(i)
    return res

def decision(new_digit):    
    n_ololo =[]
    ololo = 0
    for i in range(len(new_digit)):
        k = new_digit.index('(')+1
        j = new_digit.index(')')
    for i in range(k,j):
        n_ololo.append(new_digit[i])
    k = k-1
    for i in range(len(n_ololo)):
            if '*' in n_ololo:
                ololo = mult(n_ololo)
            elif '/' in n_ololo:
                ololo = div(n_ololo)
            elif '+' in n_ololo:
                ololo = sum(n_ololo)
            elif '-' in n_ololo:
                ololo = diff(n_ololo)   
    del new_digit[k:j+1]
    new_digit.append(ololo)

    while len(new_digit) > 1:                 
        for i in range(len(new_digit)):
            if '*' in new_digit:
                res = mult(new_digit)
            elif '/' in new_digit:
                res = div(new_digit)
            elif '+' in new_digit:
                res = sum(new_digit)
            elif '-' in new_digit:
                res = diff(new_digit)
    return res

res = decision(new_digit)
print(res)


