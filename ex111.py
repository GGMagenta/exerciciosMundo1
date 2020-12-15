# Crie um pacote chamado utilidadesCeV com módulos de moeda e dados
# transfira as funcionalidades de moeda
from ex111Dir.utilidadesCeV import moeda

preco = float(input('Digite o preço: R$'))
moeda.resumo(preco, 25, 30)
