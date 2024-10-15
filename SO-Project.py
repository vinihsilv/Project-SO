import sys

# Verifica se os argumentos foram passados
if len(sys.argv) < 3:
    print("Uso correto: python fifo.py <numero_de_frames> <sequencia_de_paginas>")
    sys.exit(1)

# Pega o número de frames da linha de comando
numero_de_frames = int(sys.argv[1])

# Pega a sequência de páginas, separa por vírgula e converte para inteiros
sequencia_de_paginas = list(map(int, sys.argv[2].split(',')))

# Exibe os valores capturados
print(f"Número de frames: {numero_de_frames}")
print(f"Sequência de páginas: {sequencia_de_paginas}")