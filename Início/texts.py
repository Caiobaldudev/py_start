#Declaração
nome_completo = "Caio Balduino"
#text / string

#Declaração string que pula linhas:
nome_completo_aspas = """John Doe
Da Silva"""

#Declaração com Quebra:
nome_completo_quebra = "John \
Doe"

name = "John"
surname = "Doe"

#Formatação
print("Nome Completo (forma 1):", name, surname)
print("Nome Completo (forma 2): " + name + surname) #sem espaço
print("Nome Completo (forma 3):" + ' first ' + "second ")
print("Nome Completo (forma 4):" + ' first',"second")
print("Nome Completo (forma 5):" + nome_completo_aspas) #com quebra
print("Nome Completo (forma 6):" + nome_completo_quebra) #sem quebra visivel no log
print("Nome Completo (forma 7): %s" % nome_completo)
print("Nome Completo (forma 8): %s %s" % (name, surname))
print(f"Nome Completo (forma 9): {name} {surname}")
print("Nome Completo (forma 10): {} {}".format(name, surname))
