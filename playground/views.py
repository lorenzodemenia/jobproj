from django.shortcuts import render
from django.http import HttpResponse


# funzione fatta da me
def parser_one(text):
    sl = text.replace(", ", " ")
    split_list = sl.rsplit(" ")  # divide la stringa in sottostringhe ogni volta che trova lo spazio e le inserisce
                                   # in una lista
    end_list = []
    count = 0
    # trovo la posizione dell'unico elemento che conosco la dimensione, siccome il cap è sempre di 5 numeri e quindi mi
    # basta contare fino a dove trovo una stringa di soli caratteri (isdigit()) e di dimensione 5
    for first_step in split_list:
        count += 1
        if first_step.isdigit() and len(first_step) >= 5:
            break

    count_second = 0
    tmp = ""
    for sl in split_list:
        count_second += 1
        list_tmp = []
        if count_second < count-1:  # vado a vedere se count_second è minore di count-1, siccome so che prima del cap
                                    # c'è il numero civico e prima di esso c'è la via che non sempre è di 2 stringhe

            tmp += sl               # concateno le stringhe
            if count_second+1 != count-1:
                tmp += " "              # inserisco anche uno spazio tra di esse
        elif count_second == count-1:   # siccome so che il numero civico si trova prima del cap
                                                        # allora vado controllo se count_second è uguale a count-1
            list_tmp.append("indirizzo")
            list_tmp.append(tmp)
            end_list.append(list_tmp)
            tmp = []
            list_tmp = []
            list_tmp.append("civico")
            list_tmp.append(sl)
            end_list.append(list_tmp)

        elif count_second == count and sl.isdigit():    # inserisce la stringa nel dizionario e controlla se è un numero
            list_tmp.append("cap")
            list_tmp.append(sl)
            end_list.append(list_tmp)

        elif count_second == count+1:
            list_tmp.append("comune")
            list_tmp.append(sl)
            end_list.append(list_tmp)     # inserisce il comune

            if count_second == len(split_list): # a volte se non viene inserita la provincia, vuol dire che il comune è
                                                # anche la provincia
                list_tmp.append("provinica")
                list_tmp.append(sl)
                end_list.append(list_tmp) # inserisce la provinica

        elif count_second == count+2:

            list_tmp.append("provinica")
            list_tmp.append(sl)
            end_list.append(list_tmp)   # inserisce la provinica

    return end_list



def say_hello(request):
    title = ("Title","Object")
    x = parser_one('via ragazzi del 99 10 35100 pd padova')

    return render(request, 'hello.html', lol=x)
