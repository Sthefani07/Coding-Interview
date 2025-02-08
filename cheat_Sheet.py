# Criando uma lista
arr = [1, 2, 3, 4, 5]

# Encontrar o tamanho da lista
print(len(arr))  # Saída: 5

# Acessar elementos da lista
print(arr[0])  # Primeiro elemento (1)
print(arr[-1])  # Último elemento (5)

# Percorrer a lista com for 
for num in arr:
    print(num)  # Imprime cada número

# Percorrer a lista com índice
for i in range(len(arr)):
    print(f'Índice {i}: {arr[i]}')

# Adicionar elementos
arr.append(6)  # Adiciona ao final
arr.insert(2, 10)  # Adiciona na posição 2

# Remover elementos
arr.remove(3)  # Remove o primeiro 3 encontrado
popped = arr.pop()  # Remove o último elemento

# Filtrar elementos
pares = [x for x in arr if x % 2 == 0]
print(pares)  # Lista apenas com números pares

# Encontrar um elemento
if 4 in arr:
    print("4 está na lista")

# Ordenar a lista
arr.sort()  # Ordena de forma crescente
arr.reverse()  # Inverte a lista

# Criar uma lista com range
nova_lista = list(range(1, 11))  # [1,2,3,4,5,6,7,8,9,10]

# Soma, máximo e mínimo
print(sum(arr))  # Soma dos elementos
print(max(arr))  # Maior número
print(min(arr))  # Menor número

# Encontrar o índice de um elemento
print(arr.index(4))  # Retorna o índice do número 4

# Contar a ocorrência de um elemento
print(arr.count(2))  # Conta quantas vezes o número 2 aparece

# Clonar uma lista
copia_lista = arr[:]

# Remover duplicatas
sem_duplicatas = list(set(arr))

# Juntar listas
outra_lista = [7, 8, 9]
lista_concatenada = arr + outra_lista

# Interseção entre listas
lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]
intersecao = list(set(lista1) & set(lista2))
print(intersecao)  # Elementos comuns: [3, 4]

# Diferença entre listas
diferenca = list(set(lista1) - set(lista2))
print(diferenca)  # Elementos em lista1 que não estão em lista2: [1, 2]

# União entre listas
uniao = list(set(lista1) | set(lista2))
print(uniao)  # Todos os elementos únicos combinados: [1, 2, 3, 4, 5, 6]
