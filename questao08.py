def extrair_dados():
    dados = open("dados.csv", 'r+')
    conteudos = dados.read()
    dados.close()
    conteudos = conteudos.splitlines()
    conteudos = conteudos[1:]
    return conteudos

def menu_carro():
    print("Modelos de carros: Chevrolet Onix, Ford Fiesta, VW Fox, VW Polo, Hyundai HB20 e Renault Sandero")
    carro = input("Informe um carro: ")
    print(f"O valor do {carro} no final de um ano será de {calculo_carro(carro)} reais")
    compara_carro()
    
def calculo_carro(carro):
    conteudos = extrair_dados()
    compra = 0
    impostos = 0
    combustivel = 0
    combustiveltotal = 0
    seguro = 0
    soma = 0
    for elemento in conteudos:
        dados_carro = elemento.split(',')
        if dados_carro[0] == carro:
            compra = float(dados_carro[1])
            impostos = float(dados_carro[2])
            combustivel = float(dados_carro[3])
            combustiveltotal = float(((10000/combustivel)*4.51))
            seguro = float(dados_carro[4])
            soma = round(compra+impostos+seguro+combustiveltotal,2)
            print(f"O custo total de compra é: {compra}")
            print(f"O custo total de impostos é: {impostos}")
            print(f"O custo com seguro é: {seguro}")
            print(f"O consumo médio do combustivel é: {combustivel}")
            return soma
        elif dados_carro[0] == carro:
            compra = float(dados_carro[1])
            impostos = float(dados_carro[2])
            combustivel = float(dados_carro[3])
            combustiveltotal = float(((10000/combustivel)*4.51))
            seguro = float(dados_carro[4])
            soma = round(compra+impostos+seguro+combustiveltotal,2)
            print(f"O custo total de compra é: {compra}")
            print(f"O custo total de impostos é: {impostos}")
            print(f"O custo com seguro é: {seguro}")
            print(f"O consumo médio do combustivel é: {combustivel}")
            return soma
        elif dados_carro[0] == carro:
            compra = float(dados_carro[1])
            impostos = float(dados_carro[2])
            combustivel = float(dados_carro[3])
            combustiveltotal = float(((10000/combustivel)*4.51))
            seguro = float(dados_carro[4])
            soma = round(compra+impostos+seguro+combustiveltotal,2)
            print(f"O custo total de compra é: {compra}")
            print(f"O custo total de impostos é: {impostos}")
            print(f"O custo com seguro é: {seguro}")
            print(f"O consumo médio do combustivel é: {combustivel}")
            return soma
        elif dados_carro[0] == carro:
            compra = float(dados_carro[1])
            impostos = float(dados_carro[2])
            combustivel = float(dados_carro[3])
            combustiveltotal = float(((10000/combustivel)*4.51))
            seguro = float(dados_carro[4])
            soma = round(compra+impostos+seguro+combustiveltotal,2)
            print(f"O custo total de compra é: {compra}")
            print(f"O custo total de impostos é: {impostos}")
            print(f"O custo com seguro é: {seguro}")
            print(f"O consumo médio do combustivel é: {combustivel}")
            return soma
        elif dados_carro[0] == carro:
            compra = float(dados_carro[1])
            impostos = float(dados_carro[2])
            combustivel = float(dados_carro[3])
            combustiveltotal = float(((10000/combustivel)*4.51))
            seguro = float(dados_carro[4])
            soma = round(compra+impostos+seguro+combustiveltotal,2)
            print(f"O custo total de compra é: {compra}")
            print(f"O custo total de impostos é: {impostos}")
            print(f"O custo com seguro é: {seguro}")
            print(f"O consumo médio do combustivel é: {combustivel}")
            return soma
        elif dados_carro[0] == carro:
            compra = float(dados_carro[1])
            impostos = float(dados_carro[2])
            combustivel = float(dados_carro[3])
            combustiveltotal = float(((10000/combustivel)*4.51))
            seguro = float(dados_carro[4])
            soma = round(compra+impostos+seguro+combustiveltotal,2)
            print(f"O custo total de compra é: {compra}")
            print(f"O custo total de impostos é: {impostos}")
            print(f"O custo com seguro é: {seguro}")
            print(f"O consumo médio do combustivel é: {combustivel}")
            return soma
        
def compara_carro():
    conteudos = extrair_dados()
    compra = 0
    impostos = 0
    combustivel = 0
    combustiveltotal = 0
    seguro = 0
    soma = 0
    menorvalor = 1000000
    modelo = ''
    for elemento in conteudos:
        dados_carro = elemento.split(',')
        compra = float(dados_carro[1])
        impostos = float(dados_carro[2])
        combustivel = float(dados_carro[3])
        combustiveltotal = float(((10000/combustivel)*4.51))
        seguro = float(dados_carro[4])
        soma = round(compra+impostos+seguro+combustiveltotal,2)
        if soma < menorvalor:
            menorvalor = soma
            modelo = dados_carro[0]
    print(f"O menor valor em 1 ano será do modelo: {modelo} e o valor será: {menorvalor}")