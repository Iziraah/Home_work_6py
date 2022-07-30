#Найти сумму чисел списка стоящих на нечетной позиции

subsequence = list(map(int,input('Введите значения цен через пробел ').split()))
b = subsequence[1::2]
print(sum(b))