from django.shortcuts import render
from django.http import HttpResponse
import json 

# la stessa funzione ma che ritorna un dizionario convertito in json , in modo tale che l'output sia come richiesto dopo
def parser_one_json(text):
    sl = text.replace(", ", " ")
    split_list = sl.rsplit(" ")  # divide la stringa in sottostringhe ogni volta che trova lo spazio e le inserisce
                                   # in una lista
    end_list = {}
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
        if count_second < count-1:  # vado a vedere se count_second è minore di count-1, siccome so che prima del cap
                                    # c'è il numero civico e prima di esso c'è la via che non sempre è di 2 stringhe

            tmp += sl               # concateno le stringhe
            if count_second+1 != count-1:
                tmp += " "              # inserisco anche uno spazio tra di esse
        elif count_second == count-1:   # siccome so che il numero civico si trova prima del cap
                                                        # allora vado controllo se count_second è uguale a count-1
            end_list["indirizzo"] = tmp
            tmp = []
            end_list["civico"] = sl

        elif count_second == count and sl.isdigit():    # inserisce la stringa nel dizionario e controlla se è un numero
            end_list["cap"] = sl

        elif count_second == count+1:

            end_list["comune"] = sl     # inserisce il comune

            if count_second+1 == len(split_list): # a volte se non viene inserita la provincia, vuol dire che il comune è
                                                # anche la provincia
                end_list["provinica"] = sl  # inserisce la provinica
                break
        elif count_second == count+2:

            end_list["provinica"] = sl   # inserisce la provinica

    return end_list

def convert_dictionary_list(diction):
    dir_elem = []
    for x, y in diction.items():
        tmp = []
        tmp.append(x)
        tmp.append(y)
        dir_elem.append(tmp)
    
    return dir_elem

def add_parse(request):
    data = {}
    title = {}
    
    if request.method == 'POST':
        elem = request.POST.get('name', None)
    else:
        elem = ''
    tmp = parser_one_json(elem)
    elem_json = json.dumps(tmp)
    data['elem_json'] = elem_json
    data["data"] = convert_dictionary_list(tmp)
    data["title"] = ("Title","Object")
    print(elem_json)
    return render(request, 'parser.html', data)



