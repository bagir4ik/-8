count = 0                                                       
alf = 'КАМЕНЬ'                                                  
for l1 in alf:                                                  
    for l2 in alf:
        for l3 in alf:
            for l4 in alf:
                for l5 in alf:
                    for l6 in alf:
                        word = l1 + l2 + l3 + l4 + l5 + l6      
                        if word[0] != 'Ь' and \
                        not('АЕ' in word or 'ЕА'in word) \
                        and word.count('К') == 0:
                            count += 1
print(count)
