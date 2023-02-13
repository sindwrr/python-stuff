import numpy as np


def apriori_s(SET, ITEMS, MIN_LEVEL):
    result = []
    temp = SET
    s = 1

    # выполняем цикл до тех пор, пока в какой-то момент
    # ни одна строка не пройдет через min_support
    while s > 0:

        # строим булеву матрицу
        L = np.zeros((len(temp), len(ITEMS)))
        for i in range(len(temp)):
            for j in range(len(ITEMS)):
                flag = True
                for k in range(len(temp[0])):
                    if temp[i][k] not in ITEMS[j]:
                        flag = False
                if flag:
                    L[i, j] = 1
                else:
                    L[i, j] = 0

        # выясняем, какие строки прошли через min_support
        A0 = np.array([sum(L[i, :]) for i in range(len(temp))])
        A = np.array([A0, [1 if i >= MIN_LEVEL else 0 for i in A0]])
        s = np.sum(A[1])

        # добавляем во вспом. массив подходящие строки
        temp_h = np.array([], dtype='object')
        for i in range(len(A[0])):
            if A[1, i]:
                temp_h = np.append(temp_h, temp[i])

        # заносим подходящие строки в конечный массив
        temp = temp_h
        result = np.append(result, temp)

        # добавляем к строкам по одному символу
        # (в соотв-ии с правилами алгоритма)
        temp_h = []
        for i in range(len(temp)):
            for j in range(i + 1, len(SET)):
                flag = True
                for k in range(len(temp[i])):
                    if temp[i][k] == SET[j]:
                        flag = False
                if flag:
                    temp_h = np.append(temp_h, temp[i] + SET[j])

        temp = temp_h

    # сортируем строки
    for i in range(len(result)):
        result[i] = ''.join(sorted(result[i]))

    # удаляем из конечного массива повторяющиеся строки
    nc_result = []
    [nc_result.append(x) for x in result if x not in nc_result]
    return nc_result


SET = 'ABCDEFG'
ITEMS = ['BDE', 'ADG', 'AEFG', 'CEG', 'ADG',
         'DF', 'BCE', 'BEG', 'ACDE', 'ABF']
MIN_LEVEL = 4

res = apriori_s(SET, ITEMS, MIN_LEVEL)

print('Результат:')
for i in res:
    print(i)
