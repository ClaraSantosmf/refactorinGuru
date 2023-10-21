# Se a extração de variáveis locais e parâmetros interferirem na extração de um método,
# Você pode Substituir Temporária por Consulta, introduzindo o Objeto como Parâmetro
# ou preservando o Objeto Inteiro.

# 01 - Substitua variáveis temporária por querys

# Cheira Mal. Aqui você tem uma variável (preco_base) posteriormente no seu código


def calculando_total(qtd, preco_item):
    preco_base = qtd * preco_item
    if preco_base > 1000:
        return preco_base * 0.95
    return preco_base * 0.98


# Refatoração: Mova a expressão inteira para um método separado
# Consulte o método em vez de usar uma variável.
# Incorpore o novo método em outros métodos, se necessário.


def calculando_total():
    if preco_item() > 1000:
        return preco_item() * 0.95
    return preco_item() * 0.98


def preco_item(qtd, preco_item):
    return qtd * preco_item


# Apesar de acionar duas vezes a mesma função, o compilador ou interpretador
# vai otimizar isso e criar uma variável local.
# Seu objetivo é escrever código claro.

# 02 - Utilize objetos como parametros

# Cheira mal


def calculo_ferias(data_inicio, data_fim):
    saldo_ferias(data_inicio, data_fim)
    terco_ferias(data_inicio, data_fim)
    rescisao(data_inicio, data_fim)


# Refatoração: use um mesmo objeto


def calculo_ferias(data_range):
    saldo_ferias(data_range)
    terco_ferias(ddata_range)
    rescisao(data_range)


# 02 - Preserve objetos inteiros
# Problema, você pega diversos valores do objeto e passa como parametro.


def calcula_range_ferias(data_range):
    primeiro_dia = data_range.primeiro_dia
    segundo_dia = data_range.segundo_dia
    autorizacao = verifica_autorizacao(primeiro_dia, segundo_dia)
    return autorizacao


# Refatoração: passa o objeto inteiro


def calcula_range_ferias(data_range):
    autorizacao = verifica_autorizacao(primeiro_dia, segundo_dia)
    return autorizacao
