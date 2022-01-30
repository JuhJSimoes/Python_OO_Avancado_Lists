import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
    
    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""
    
    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia!")
        
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError('A URL não é válida.')
        
    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[0:indice_interrogacao]
        return url_base
    
    def get_url_params(self):
        indice_interrogacao = self.url.find('?')
        url_params = self.url[indice_interrogacao+1:]
        return url_params
    
    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_params().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca)+1
        indice_e_comercial = self.get_url_params().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_params()[indice_valor:]    
        else:
            valor = self.get_url_params()[indice_valor:indice_e_comercial]
        
        return valor
    
    def __len__(self):
        return len(self.url)
    
    def __str__(self):
        return self.url
        
    def __eq__(self, other):
        return self.url == other.url

 
url = 'bytebank.com/cambio?quantidade=100&moedaDestino=real&moedaOrigem=dolar'
extrator_url = ExtratorURL(url)
extrator_url_2 = ExtratorURL(url)
print("O tamanho da URL é: ", len(extrator_url))
print(extrator_url)
print("extrato_url == extrator_url_2? ", extrator_url == extrator_url_2, '\n')


print('############### DESAFIO ################ \n' )
#DESAFIO############

valor_dolar=5.50
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
valor_quantidade = extrator_url.get_valor_parametro("quantidade")

if moeda_origem == 'real' and moeda_destino == 'dolar':
    valor_conversao = int(valor_quantidade)/valor_dolar
    print('O valor de R$ ' + valor_quantidade + " reais é igual a $ " + str(valor_conversao) + " dolares.")
elif moeda_origem == 'dolar' and moeda_destino == 'real':
    valor_conversao = int(valor_quantidade)*valor_dolar
    print('O valor de $ ' + valor_quantidade + " dolar é igual a R$ " + str(valor_conversao) + " reais.")
else:
    print(f'Cambio de {moeda_origem} para {moeda_destino} não está disponivel.')
