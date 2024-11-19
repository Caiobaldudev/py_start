#Funções exemplo
def saudacao(nome):
  print(f"Olá, {nome}!")

print("\n Chamando a função saudação: ")
saudacao("alice")
saudacao("bob")

# Funcao com retorno
def quadrado(numero):
  resultado = numero ** 2
  return resultado

print("Função quadrado: ")
print("1º Resultado:", quadrado(3)) 
atribuicao_quadrado = quadrado(5) #quadrado(n)
print("Novo resultado:", quadrado(6))

# Função com multiplos parametros
def soma(n1,n2):
  resultado = n1 + n2
  return resultado

print("Chamando a função soma: ")
n1 = 20
n2 = 30
result_soma = soma(n1,n2)
print("Resultado da soma dos números:", result_soma)
print("A Soma do número %s e o numero %s é %s" % (n1, n2, result_soma))