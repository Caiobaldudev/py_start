#Dicionários
pessoa = {"name": "John", "surname": "Doe", "age": 30}

print("exemeplo de dicionario: ", pessoa)
print("Valor pego por chave:", pessoa["name"])
print("Valor pego por chave:", pessoa["surname"])

#atribuir depois da instância
pessoa["city"] = "São Paulo"
print(pessoa)
#também posso re-atribuir algum valor

#remover um par chave-valor
del pessoa["city"]
print("removi uma chave-valor: ",pessoa)

#Métodos: keys(), values(), items()
#keys
personKeys = pessoa.keys()
print("Chaves dicionário:", personKeys)
#print("Chaves dicionário:", personKeys[0]) tem que passar para lista: list(pessoa.keys())

#values
valores = pessoa.values()
print("Valores do dicionário:", valores)

#items
itens = pessoa.items()
print("Itens do dicionário chave-valor", itens)

