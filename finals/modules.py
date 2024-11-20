print("Exemplo de importação de um módulo padrão:")
import math
from math import sqrt

raiz_quadrada = math.sqrt(25)
print(f"A raiz quadrada do número é: {raiz_quadrada}")

#com o modo de importar especificamente
raiz_quadrada = sqrt(25)
print(f"A raiz quadrada do número é: {raiz_quadrada}")

print("\nExemplo de criação e utilização de um módulo personalizado")
import my_module #ou posso importar de modo específico

mensagem = my_module.saudacao("Caio")
resultado_dobro = my_module.dobro(5)
print(mensagem)
print(resultado_dobro)