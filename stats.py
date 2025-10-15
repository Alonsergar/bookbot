def count_words(text:str):
    text=text.split()
    total_words=len(text)
    return total_words


    
def count_char(text:str):
    diccionario={}
    text=text.lower()
    for char in text:
        if char not in diccionario:
            diccionario[char]=0
        if char in diccionario:
            diccionario[char]=diccionario[char]+1
    return diccionario


def sort_on(items):
    return items["num"]


def show_report(dic,num_words):
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    new_dic={"char":"","num":""}
    #debemos coger el diccionariio con los  char y sus valores
    # creamos una lista de deccionarios y cada diccionario tiene dos keys: char y num y luego sus respectivos valores
    lista=[]
    #lo que pasa es que al cambiar el valor, luego cambia en el append, como hago que no cambie?
    for i in dic:
        new_dic={"char":"","num":""}
        new_dic["char"]=i
        new_dic["num"]=dic[i]
        lista.append(new_dic)
        # vale, solo tenía que meter la creación del diccionario dentro de cada iteración
        # bien ahora solo nos hace falta ordenarlo conforme al num

    
    lista.sort(reverse=True,key=sort_on)

    # vale voy a explicar a ver si me he enterado, cuando tú usas sort_on como la key, lo que hace pythons es que por ejemplo, coge el primer item de la lista
    # y dece vale lo voy a ordenar, y como la key para ordenarlo es sort_on llama a esa función con ese item de la lista y la función devuelve un num
    # ya ese num lo deja en una posición y conforme se vayan añadiendo números se irán ordenando los demás
        
    for i in lista:
        print(f"{i["char"]}: {i["num"]} \n")

    
