import sys


if len(sys.argv) < 3:
    print("Uso correto: python fifo.py <numero_de_frames> <sequencia_de_paginas>")
    sys.exit(1)

numero_de_frames = int(sys.argv[1])
sequencia_de_paginas = list(map(int, sys.argv[2].split(',')))
lista_memoria = [-1] * numero_de_frames
def FIFO(sequencia_de_paginas,lista_memoria):
    fila = []
    for i in range(len(sequencia_de_paginas)):
        if(sequencia_de_paginas[i] in lista_memoria):
            print("ja tem")
        else:
            if(-1 in lista_memoria):
                vazio=lista_memoria.index(-1)
                lista_memoria[vazio] = sequencia_de_paginas[i]
                fila.append(sequencia_de_paginas[i])
            else:
                page_removida=fila.pop(0)
                index_removido = lista_memoria.index(page_removida)
                lista_memoria[index_removido] = sequencia_de_paginas[i]
                fila.append(sequencia_de_paginas[i])
            print(f"Page fault! Página {sequencia_de_paginas[i]} carregada: {lista_memoria}")
    print(f"\nNúmero de frames: {numero_de_frames}")
    print(f"Sequência de páginas: {sequencia_de_paginas}")
    print(f"Estado final da memória: {lista_memoria}") 

def OPT(sequencia_de_paginas, lista_memoria):
    fila = []
    for i in range(len(sequencia_de_paginas)):
        pagina_atual = sequencia_de_paginas[i]
        if(sequencia_de_paginas[i] in lista_memoria):
            print("ja tem")
            
        else:
            if(-1 in lista_memoria):
                vazio=lista_memoria.index(-1)
                lista_memoria[vazio] = pagina_atual
                fila.append(pagina_atual)
            else:
                fila.clear()
                for elemento in lista_memoria:
                    if elemento in sequencia_de_paginas[i+1:]:
                            index = sequencia_de_paginas[i+1:].index(elemento) + i + 1
                            fila.append(index)  # Adiciona o próximo uso à fila
                    else:
                        fila.append(float('inf'))  # Página não será usada novamente
                        
                    # Encontrar a página que não será usada por mais tempo
                alteração = fila.index(max(fila))
                lista_memoria[alteração] = pagina_atual
                
                
            print(f"Page fault! Página {sequencia_de_paginas[i]} carregada: {lista_memoria}")
    print(f"\nNúmero de frames: {numero_de_frames}")
    print(f"Sequência de páginas: {sequencia_de_paginas}")
    print(f"Estado final da memória: {lista_memoria}")

def LRU(sequencia_de_paginas, lista_memoria):
    fila = []
    for i in range(len(sequencia_de_paginas)):
        pagina_atual = sequencia_de_paginas[i]
        if(sequencia_de_paginas[i] in lista_memoria):
            print("ja tem")
            
        else:
           
            if(-1 in lista_memoria):
                vazio=lista_memoria.index(-1)
                lista_memoria[vazio] = pagina_atual
                fila.append(pagina_atual)
            else:
                fila = []
                for pagina in lista_memoria:
                    if pagina in sequencia_de_paginas[:i]:
                        aux = sequencia_de_paginas[:i].index(pagina)
                        fila.append(aux)
                if fila: 
                    alteracao = min(fila)
                    lista_memoria[lista_memoria.index(sequencia_de_paginas[alteracao])] = pagina_atual
            print(f"Page fault! Página {sequencia_de_paginas[i]} carregada: {lista_memoria}")
    print(f"\nNúmero de frames: {numero_de_frames}")
    print(f"Sequência de páginas: {sequencia_de_paginas}")
    print(f"Estado final da memória: {lista_memoria}")
                    

LRU(sequencia_de_paginas,lista_memoria)  

