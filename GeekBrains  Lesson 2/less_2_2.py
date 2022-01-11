'''
Посчитать четные и нечетные цифры введенного натурального числа
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
'''
def couter_value():
    cont_0 = 0
    cont_1 = 0
    while True:
        a = str(input('Введите число- '))
        for i in a:
            if int(i)%2 ==0:
                cont_0+=1
            else:
                cont_1+=1
        return f'Четних - {cont_0} і нечетних - {cont_1}'



print(couter_value())