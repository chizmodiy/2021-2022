"""
1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается,
а запрашивает новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '', '/'), программа должна
сообщать об ошибке и снова запрашивать знак операции. Также она должна сообщать пользователю о невозможности деления
на ноль, если он ввел его в качестве делителя.
"""


def calc_fnc():
    def calculate(a,b,c):
        if c == '+':
            return a+b
        if c == '-':
            return a-b
        if c == '*':
            return a*b
        if c == '/':
            if a == 0 :
                return 'Error #2 0 in znamenik'
            else:
                return a/b
    acceptedValue = ['0','+','-','/','*']
    while True:
        answsr_A = int(input('Введите 1 число:'))
        answsr_B = int(input('Введите 2 число:'))
        answsr_C = str(input('Введите знак : '))
        if answsr_C == str(0):
                break
        if str(answsr_C) not in acceptedValue:
                return 'Error#1 Invalid value'
        else:
                return calculate(answsr_A,answsr_B,answsr_C)


if __name__ =='__main__':
    print(calc_fnc())