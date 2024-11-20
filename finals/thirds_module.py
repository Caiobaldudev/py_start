# Biblioteca Request (HTTP)
# Abrir o terminal:
#pip3 install requests -> podemos especificar a versão que queremos com:
# pip3 install requests==2.31.0 (exemplo)

print("\nImportação e uso de um módulo de terceiros")
import requests

url = "https://www.example.com"
response = requests.get(url)
print(f"Solicitação HTTP para {url} retornou o status {response.status_code}")