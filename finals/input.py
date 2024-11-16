#Função input para entrada de dados

age = int(input("Digite sua idade: "))
if age >= 18:
  print("Pode dirigir.")
else:
  print("Não pode dirigir.")

if age >= 18:
  print("Você tem a maioridade!")
elif age >= 12:
  print("Você é um adolescente!")
else:
  print("Você é muito novo!!")