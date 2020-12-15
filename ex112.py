# No pacote dados crie uma função leiaDinheiro para validar apenas valores monetários
from ex112Dir.utilidadesCeV import moeda
from ex112Dir.utilidadesCeV import dados

preco = dados.leiaDinheiro("Digite um valor: R$")
moeda.resumo(preco, 15, 45)
