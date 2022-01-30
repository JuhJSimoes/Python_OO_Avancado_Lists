#url = 'http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'
from ast import If


#url = 'bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real'

url =" "

#Sanitização da URL
url = url.replace(' ','')

#Validação da URL
if url == "":
    raise ValueError("A URL está vazia")

#Separa base e os parametros
indice_interrogacao = url.find('?')
url_base = url[0:indice_interrogacao]
url_params = url[indice_interrogacao+1:]
print(url_params)

#Busca o valor de um parametro
parametro_busca = 'moedaOrigem'
indice_parametro = url_params.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca)+1
indice_e_comercial = url_params.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_params[indice_valor :]    
else:
    valor = url_params[indice_valor:indice_e_comercial]
print(valor)