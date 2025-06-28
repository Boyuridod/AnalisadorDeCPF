# Autor: Yuri David Silva Duarte
# Instaram: @yuridsduarte
# Linkedin: https://www.linkedin.com/in/yuri-duarte-050581208/

# Função que descobre a região fiscal
def descobreRegiao(n):

    if(n == 1): return "1) DF, GO, MS, MT e TO"
    elif(n == 2): return "2) AC, AM, AP, PA, RO e RR"
    elif(n == 3): return "3) CE, MA e PI"
    elif(n == 4): return "4) AL, PB, PE, RN"
    elif(n == 5): return "5) BA e SE"
    elif(n == 6): return "6) MG"
    elif(n == 7): return "7) ES e RJ"
    elif(n == 8): return "8) SP"
    elif(n == 9): return "9) PR e SC"
    elif(n == 0): return "0) RS"

# Função que faz a análise do CPF
def analisaCPF(cpf):
    cpf = list(cpf)

    cpf = [int(c) for c in cpf if c.isdigit()]

    analise = {
        "valido": False,
        "regiao": None
    }

    if(len(cpf) == 11):
        teste = 0

        # Calculo do 1° digito verificador
        for i in range(9):
            teste += cpf[i] * (10 - i)

        if((teste % 11) < 2):
            teste = 0

        else:
            teste = 11 - (teste % 11)

        # Calculo do 2° digito verificador
        if(cpf[9] == teste):
            teste = 0

            for i in range(0, 10):
                teste += cpf[i] * (11 - i)

            if((teste % 11) < 2):
                teste = 0
            else:
                teste = 11 - (teste % 11)

            if((cpf[10]) == teste):
                analise["valido"] = True
                analise["regiao"] = descobreRegiao(cpf[8]) # Teste do 9° Dígito (Dígito da região fiscal)

    return analise

# print(analisaCPF("529.982.247-25")) # Válido | Região 7
# print(analisaCPF("52998224725")) # Válido | Região 7
# print(analisaCPF("123.456.654-01")) # Inválido
# print(analisaCPF("12345678901")) # Inválido
# print(analisaCPF("456")) # Inválido
# print(analisaCPF("123,456-01")) # Inválido