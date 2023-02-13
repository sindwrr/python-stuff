import numpy as np
from trie import *

def fpgrowth_s(SET, ITEMS, MIN_LEVEL):
    result = []
    SET = list(SET)
    
    # находим support каждого символа
    count = np.zeros(len(SET))
    L = np.zeros((len(SET), len(ITEMS)))
    for i in range(len(SET)):
        for j in range(len(ITEMS)):
            if SET[i] in ITEMS[j]:
                count[i] += 1

    # сортируем символы по частоте (support)
    for i in range(len(count)):
        min = i
        for j in range(i + 1, len(count)):
            if count[min] < count[j]:
                min = j
        count[i], count[min] = count[min], count[i]
        SET[i], SET[min] = SET[min], SET[i]
    for i in range(len(SET)):
        for j in range(i+1, len(SET)):
            if count[i] == count[j] and SET[i] > SET[j]:
                SET[i], SET[j] = SET[j], SET[i]

    # сортируем транзакции на основе support каждого символа
    for i in range(len(ITEMS)):
        for j in range(len(ITEMS[i])):
            for k in range(j+1, len(ITEMS[i])):
                if SET.index(ITEMS[i][j]) > SET.index(ITEMS[i][k]):
                    l = list(ITEMS[i])
                    l[j], l[k] = l[k], l[j]
                    ITEMS[i] = ''.join(l)

    # строим изначальное дерево
    init_tree = constructTree(ITEMS)

    # для каждого символа, прошедшего min_support, строим
    # строим условное дерево, и дальше по рекурсии
    SET = SET[::-1]
    for r in SET:
        if init_tree.occur(r) >= MIN_LEVEL:
            result = np.append(result, r)
            cond_strings = cond_tree(SET, ITEMS, r, MIN_LEVEL)
            if len(cond_strings) > 0:
                result = np.append(result, cond_strings)

    # сортируем каждую строку по алфавиту
    for i in range(len(result)):
        if len(result[i]) > 1:
            for j in range(len(result[i])):
                for k in range(j+1, len(result[i])):
                    if result[i][j] > result[i][k]:
                        l = list(result[i])
                        l[j], l[k] = l[k], l[j]
                        result[i] = ''.join(l)

    return result

SET = 'ABCDEFG'
ITEMS = ['BDE', 'ADG', 'AEFG', 'CEG', 'ADG',
         'DF', 'BCE', 'BEG', 'ACDE', 'ABF']
MIN_LEVEL = 3

res = fpgrowth_s(SET, ITEMS, MIN_LEVEL)

print('Результат:')
for i in res:
    print(i)