endereco = "Rua Paulo Roberto Roberto da Silva Nogueira 648, Sulacap, Rio de Janeiro, RJ, 21746-090"

import re #importando REGEX

padrao = re.compile('[0-9]{5}[-]{0,1}[0-9]{3}')
busca = padrao.search(endereco) #match ou none

if busca:
    cep = busca.group()
    print(cep)