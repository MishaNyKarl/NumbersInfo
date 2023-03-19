

def numbers_info(x1,x2):
    """Функция для нахождения множителей двух числе, их общих множителей,
     Наибольшего Общего Делитеял и Наименьшего Общего Кратного"""

    mnoj_x1 = []
    ch1 = x1
    for i in range(2,ch1+1):
        for j in range(int(ch1**0.5)):
            if ch1 % i == 0:
                mnoj_x1.append(i)
                ch1 = ch1 // i
    # print(x1, '=',mnoj_x1)

    mnoj_x2 = []
    ch2 = x2
    for i in range(2, ch2+1):
        for j in range(int(ch2 ** 0.6)):
            if ch2 % i == 0:
                mnoj_x2.append(i)
                ch2 = ch2 // i
    # print(x2, '=',mnoj_x2)

    com_mul = []
    for i in range(len(mnoj_x1)):
        for j in range(i,len(mnoj_x2)):
            if mnoj_x1[i] == mnoj_x2[j]:
                com_mul.append(mnoj_x1[i])
                break
    # print('Общие множители =', com_mul)

    nod = 1
    for i in range(len(com_mul)):
        nod = nod * com_mul[i]
    # print('НОД =',nod)

    nok = 1
    max_list = []
    min_list = []
    if len(mnoj_x1) >= len(mnoj_x2):
        for i in range(len(mnoj_x1)):
            max_list.append(i)
        for i in range(len(mnoj_x2)):
            min_list.append(i)
    else:
        for i in range(len(mnoj_x2)):
            max_list.append(i)
        for i in range(len(mnoj_x1)):
            min_list.append(i)

    nok_list = min_list
    rep_in_lists = False
    for i in max_list:
        for j in min_list:
            if i == j:
                rep_in_lists = True

    if rep_in_lists == True:

        nok = 1
        for i in max_list:
            if i in min_list:
                nok_list.remove(i)
        for i in range(len(nok_list)):
            nok = nok * nok_list[i]
        nok = nok * max(x1, x2)
    else:
        nok = x1 * x2

    # print('НОК =',nok)

    print(f'Числa {x1} = {mnoj_x1} и {x2} = {mnoj_x2}, с общими множителями {com_mul}, НОД = {nod}, НОК = {nok}')


numbers_info(12324,23412)
