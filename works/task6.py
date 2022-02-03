import math
import sys
sys.setrecursionlimit(5000)
# laba5(1)
def fnc_5_1(x,n):
    i = 1
    result = 0
    while i != n:
        result += (2 * n) / (a * (a + n))
        i += 1
    return result

# laba5(2)
def func5_2():
    pass
# laba5(3)
def func5_3(x,n):
    i= 1
    result= 1
    while i !=n:
        result *= 1-(4*x**2/((2*n-1)**2 * 3.14))
        i+=1
    return int(result) == int(math.cos(x))








# laba6(1)
def func6_1(giperPL:list):
    start= 0
    for x in giperPL:
        if x < 0:
            start = x
            break
        else:
            continue
    result= [x for x in giperPL[giperPL.index(start):] if x <0]
    return len(result)

# laba6(2)
def func6_2()->list:
    result= []
    n= int(input('Enter the number  '))
    if n<1:
        raise ValueError('Values greater than 0')
    else:
        i=1
        while i != n:
            x = (((-1)**i)*i)/2
            result.append(x)
            i+=1
        result = sum([x for x in result if x >0 ])
        return result

# laba6(3) хз хуйня єбана
def func6_3(a:int, n:int):
    pass










# laba8(1)
def diskriminant(a_1 ,b_1, c_1 ,a_2,b_2,c_2):
    discr_1 = b_1**2 - 4*a_1*c_1
    discr_2 = b_2**2 - 4*a_2*c_2
    print('\nFirst result')
    if discr_1 > 0:
        x1 = (-b_1 + math.sqrt(discr_1)) / (2 * a_1)
        x2 = (-b_1 - math.sqrt(discr_1)) / (2 * a_1)
        print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
    elif discr_1 == 0:
        x = -b_1 / (2 * a_1)
        print("x = %.2f" % x)
    else:
        print("Корней нет")
    print('\nSecond result')
    if discr_2 > 0:
        x1 = (-b_2 + math.sqrt(discr_2)) / (2 * a_2)
        x2 = (-b_2 - math.sqrt(discr_2)) / (2 * a_2)
        print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
    elif discr_2 == 0:
        x = -b_2 / (2 * a_2)
        print("x = %.2f" % x)
    else:
        print("Корней нет")
# a_1 = -4
# a_2 = -1
# print(diskriminant(a_1, 2, 7,a_2,-5,2))


# laba8(2)

def IsArithmeticProgression(list_:list , n =4):
    y=[]
    count = 0
    clear_lt= []
    for x in list_:
        if  not isinstance(x,int):
            raise ValueError("Enter an integer!1")
            exit()
        else:
            if len(list_)<4:
                raise ValueError('4 numbers are required to determine the progression!2')
                exit()
            else:
                continue
    f = lambda list, n=4: [list_[i:i + n] for i in range(0, len(list_), n)]
    f= [x for x in f(list_) if len(x)==4]
    for x in f:
        d =x[1]-x[0]
        if x[3]==x[2]+d ==x[0]+3*d:
            count+=1
    return f'Result - {count}'
# print(IsArithmeticProgression([0, 1, 2, 3, 3, 5, 7, 9, 6, 54, 3, 2, 2, 1], 4))


# laba8(3)
def requer(i:int):
    if i==0:
        return 0
    if i==1:
        return 7
    else:
        x_n = requer(i-1)*(1+ requer(i-2))
        return x_n

