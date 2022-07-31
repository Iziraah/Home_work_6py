# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.

input_str = '2+2*2'
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


