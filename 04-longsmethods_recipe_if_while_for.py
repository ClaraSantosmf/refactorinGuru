# Operações condicionais e loops são boas soluções para colar o código
# e conseguir mover para um método separado
# Para condicional, use a decomposição condicional.
# Para loops, tente extrair o method.

# 01 - Decomposição condicional
# Cheira mal. Você tem um complexo if e else.


def calculo_salario(range_data, salario):
    if range_data.inicio > 20 and range_data.final < 30:
        terco_ferias = salario / 3
        salario = salario + terco_ferias
        comissao = salario * 0.05
        return salario + comissao
    else:
        comissao = salario * 0.05
        return salario + comissao


# Refatoração: Decompanha as partes mais complexas em métodos


def permissao_comecar_ferias(range_data):
    if range_data.inicio > 20 and range_data.final < 30:
        return True
    return False


def calcular_salario_com_ferias_comissao(salario):
    terco_ferias = salario / 3
    salario = salario + terco_ferias
    comissao = salario * 0.05
    return salario + comissao


def calcular_apenas_salario_comissao(salario):
    return salario + (salario * 0.05)


def calculo_salario(range_data, salario):
    if permissao_comecar_ferias(range_data):
        return calcular_salario_com_ferias_comissao(salario)
    else:
        return calcular_apenas_salario_comissao(salario)


# 02 - Extraia o método com um loop

# Cheira mal: dentro de um loop existe uma lógica complexa


def imprimirPropriedades(usuarios):
    for i in range(len(usuarios)):
        resultado = ""
        resultado += usuarios[i].getNome()
        resultado += " "
        resultado += str(usuarios[i].getIdade())
        print(resultado)
        # ...


# Refatoração: Decompanha as partes mais complexas em métodos


def imprimirPropriedades(usuarios):
    for usuario in usuarios:
        print(obterPropriedades(usuario))
        # ...


def obterPropriedades(usuario):
    resultado = ""
    resultado += usuarios[i].getNome()
    resultado += " "
    resultado += str(usuarios[i].getIdade())
    return resultado


# Entre todos os tipos de código orientado a objetos,
# as classes com métodos curtos têm o maior retorno. 
# Quanto mais longo for um método ou função, mais difícil se torna compreendê-lo e mantê-lo.