import sys


if len(sys.argv) < 4:
    print("Uso correto: python SO-Project.py <numero_de_frames> <sequencia_de_paginas> <algoritmo_desejado>")
    sys.exit(1)

numero_de_frames = int(sys.argv[1])
sequencia_de_paginas = list(map(int, sys.argv[2].split(',')))
algoritmo_desejado = sys.argv[3]  
lista_memoria = [-1] * numero_de_frames

def imprime_saída(i, acerto):
    for f in range(numero_de_frames):
                if(lista_memoria[f] == sequencia_de_paginas[i]):
                    print(f"[{lista_memoria[f]}] <- ({acerto})")
                else:
                    print(f"[{lista_memoria[f]}]")
    print("\n")

def FIFO(sequencia_de_paginas,lista_memoria):
    fila = []
    hit_rate = 0
    miss_rate = 0
    for i in range(len(sequencia_de_paginas)):
        print(f"page: {sequencia_de_paginas[i]}")
        if(sequencia_de_paginas[i] in lista_memoria):
            imprime_saída(i, "hit")
            hit_rate += 1
        else:
            if(-1 in lista_memoria):
                vazio=lista_memoria.index(-1)
                lista_memoria[vazio] = sequencia_de_paginas[i]
                fila.append(sequencia_de_paginas[i])
                miss_rate += 1

            else:
                page_removida=fila.pop(0)
                index_removido = lista_memoria.index(page_removida)
                lista_memoria[index_removido] = sequencia_de_paginas[i]
                fila.append(sequencia_de_paginas[i])
                miss_rate += 1
            imprime_saída(i, "miss")
    print(f"Hit rate: ({hit_rate}/{len(sequencia_de_paginas)})")
    print(f"Miss rate: ({miss_rate}/{len(sequencia_de_paginas)})")


def OPT(sequencia_de_paginas, lista_memoria):
    fila = []
    hit_rate = 0
    miss_rate = 0
    for i in range(len(sequencia_de_paginas)):
        print(f"page: {sequencia_de_paginas[i]}")
        pagina_atual = sequencia_de_paginas[i]
        if(sequencia_de_paginas[i] in lista_memoria):
            imprime_saída(i, "hit")
            hit_rate += 1
            
        else:
            if(-1 in lista_memoria):
                vazio=lista_memoria.index(-1)
                lista_memoria[vazio] = pagina_atual
                fila.append(pagina_atual)
                miss_rate += 1
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
                miss_rate += 1

                
                
            imprime_saída(i, "miss")
    print(f"Hit rate: ({hit_rate}/{len(sequencia_de_paginas)})")
    print(f"Miss rate: ({miss_rate}/{len(sequencia_de_paginas)})")

def LRU(sequencia_de_paginas, lista_memoria):
    fila = []
    hit_rate = 0
    miss_rate = 0
    for i in range(len(sequencia_de_paginas)):
        print(f"page: {sequencia_de_paginas[i]}")
        pagina_atual = sequencia_de_paginas[i]
        if(sequencia_de_paginas[i] in lista_memoria):
            imprime_saída(i, "hit")
            hit_rate += 1
            
        else:
           
            if(-1 in lista_memoria):
                vazio=lista_memoria.index(-1)
                lista_memoria[vazio] = pagina_atual
                fila.append(pagina_atual)
                miss_rate += 1
            else:
                fila = []
                for pagina in lista_memoria:
                    if pagina in sequencia_de_paginas[:i]:
                        lista_reversa = list(reversed(sequencia_de_paginas[:i]))
                        aux = lista_reversa.index(pagina)
                        fila.append(i - 1 - aux)
                if fila: 
                    alteracao = min(fila)
                    lista_memoria[lista_memoria.index(sequencia_de_paginas[alteracao])] = pagina_atual
                    miss_rate += 1
            imprime_saída(i, "miss")
    print(f"Hit rate: ({hit_rate}/{len(sequencia_de_paginas)})")
    print(f"Miss rate: ({miss_rate}/{len(sequencia_de_paginas)})")
                    
if(algoritmo_desejado == "FIFO"):
    FIFO(sequencia_de_paginas,lista_memoria)
elif(algoritmo_desejado == "OPT"):
    OPT(sequencia_de_paginas,lista_memoria)
elif(algoritmo_desejado == "LRU"):
    LRU(sequencia_de_paginas, lista_memoria)
 

