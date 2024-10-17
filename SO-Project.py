import sys


if len(sys.argv) < 3:
    print("Uso correto: python fifo.py <numero_de_frames> <sequencia_de_paginas>")
    sys.exit(1)

numero_de_frames = int(sys.argv[1])
sequencia_de_paginas = list(map(int, sys.argv[2].split(',')))
lista_memoria = [-1] * numero_de_frames
count = 0 
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
