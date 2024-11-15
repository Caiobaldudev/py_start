#Declaração
list = [1, 2, 3, "four", True, False]
print("example: ", list) #lista completa
print(list[3]) #pegando um elemento da lista
print(list[1:5]) #pegando elementos através de índices
print(list[:3]) #pegando elementos através de índices (sem colocar o indicador inicial) - quando queremos ver do início da lista
print(list[2:]) #pegando elementos através de índices (somente com indicador inicial) - quando queremos ver de um elemento específico até o final

#Mudando um elemento da lista
list[0] = "python"
print(list)

#Adicionar elemento ao final
list.append("hello")
print(list)


second_list = [1,2,3,4,5]
#Retorna o índice do elemento especificado:
i = second_list.index(4)
print(i)

#insert
second_list.insert(3, 3.5) #escolhe um índice, ele entra no lugar e empurra o próximo!
print(second_list)

#exlcuir
second_list.pop(3) #exclui um item da lista - tirei o 3.5
print(second_list)

#remove
second_list.remove(5) #mudo a estrutura da lista, escolho diretamente qual elemento quero remover
print(second_list)

#organizar
second_list.sort(reverse=True) #só com o sort() ele organiza em ordem crescente
print(second_list)


