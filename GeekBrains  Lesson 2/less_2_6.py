# 7. Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# # 1+2+...+n = n(n+1)/2, где n — любое натуральное число


def some_fnc(num: int):
    frst_sum = 0
    scnd_sum = 0
    for i in range(num+1):
        frst_sum += i
    scnd_sum = (num*(num+1))/2
    return frst_sum==scnd_sum


print(some_fnc(121))
