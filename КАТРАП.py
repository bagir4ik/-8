alf = 'СПАРТАК'                                             #задаем алфавит допустимых букв
a = []                                                      #создаем список (массив) для названий
for x1 in alf:                                              #перебираем все 6 букв названия
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                for x5 in alf:
                    for x6 in alf:
                        s = x1 + x2 + x3 + x4 + x5 + x6     #собираем слово из переменных
                        if ('КАТ' in s or 'ТАК' in s) and \
                           ('ПАР' in s or 'РАП' in s):      #проверка на букву Эрика между буквами жены и друга
                            a.append(s)                     #при выполнении условия добавляем слово в список
print(a[0][::-1])                                           #вывод первого слова из списка задм наперед
    
from itertools import product                                       #импортируем функцию product() из модуля itertools
for x in product('СПАРТАК', repeat=6):                              #перебираем значения для переменной х из алфавита 6 раз
    s = ''.join(x)                                                  #приписываем букву (х) в слово
    if ('КАТ' in s or 'ТАК' in s) and ('ПАР' in s or 'РАП' in s):   #проверка на условия любимых букв
        print(''.join(reversed(s)))                                 #вывод слова, если оно подходит с обратным порядком слов
        break                                                       #прерывание цикла, так как нужно первое значение
