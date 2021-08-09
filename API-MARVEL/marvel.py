# Bibliotecas a serem importadas
import hashlib  # Realizar a MD5
import time   # Coletar o tempo
import requests # Biblioteca que faz requisicoes, utilizada para acessar a Marvel
 
# Chaves da API para a aplicação
particular = "ba92b596fe82edfdbad2d946f2d4565d987786b4" # Chave particular (private key)
publica = "49ecef7dc3cb29cae1b7b4b6c089a509" # Chave publica (public key)
 
# Construindo o MD5
m = hashlib.md5()  # Chamando a funcao para criptografar
 
ts = str(time.time())   # Coleta o tempo atual
 
# Adiciona todos as parcelas da criptografia na forma de bytes
m.update(bytes(ts, 'utf-8'))  # O tempo atual
m.update(bytes(particular, 'utf-8')) # A chave particular (private key)
m.update(bytes(publica, 'utf-8')) # Adiciona a chave publica (public key)
 
hasht = m.hexdigest() # Cria o MD5
 
# Montando URL da requisicao
base = "https://gateway.marvel.com"  # Pagina base para todas as requisicoes
 
personagem = input("Digite o nome em ingles do personagem: \n") # Pede pro usuario digitar o nome
requisicao = "/v1/public/stories?comics=" + personagem + "&orderBy=name&limit=1"  # O que eu quero da requisicao
 
# Juntando todas as partes da URL
URL = base + requisicao +"&ts=" + ts+ "&apikey=" + publica + "&hash=" + hasht
 
# Fazendo a requisicao
dados = requests.get(URL).json() # Os dados sao recebidos a partir da requisicao
 
# Voce pode descomentar a linha abaixo para ver como os dados sao recebidos a partir da requisicao
#print(dados)
 
# Verifica se existe uma descrição dentro dos dados recebidos
try:
    descricao = dados["data"]["results"][0]["description"]
except: # Se nao existe
    exit("Voce digitou um personagem invalido") # Avisa o usuario do erro e para o programa
 
print(descricao) # Apresentamos na tela esse resultado