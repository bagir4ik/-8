count = 0                                                       #создаем счетчик
alf = 'КАМЕНЬ'                                                  #создаем доступный алфавит 
for l1 in alf:                                                  #прогоняем все буквы от 1 до 6
    for l2 in alf:
        for l3 in alf:
            for l4 in alf:
                for l5 in alf:
                    for l6 in alf:
                        word = l1 + l2 + l3 + l4 + l5 + l6      #создаем слово из букв
                        if word[0] != 'Ь' and \
                        not('АЕ' in word or 'ЕА' in word):      #первая буква не 'Ь' и отсутствие гласных рядом
                            count += 1                          #если выполняется условие, то счётчик+1
print(count)                                                    #вывод счетчика
