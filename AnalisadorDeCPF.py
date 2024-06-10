# Declaração de variáveis
CPF = ""
digitos = []
isCorreto = True
teste = 0

# Função que descobre a região fiscal
def DescobreRegiao(n):

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

# Receber os dados
while(True):
    CPF = input("Digite seu CPF: ")

    if(len(CPF) != 11 and len(CPF) != 14):
        print("Quantidade de caracteres insuficiente!")

    try:
        # Converter os dados
        for i in CPF:
            if(i != "." and i != "-"):
                digitos.append(int(i))

        break

    except:
        print("Confira se todos os caracteres digitados são números!")

# Processando os dados

for i in range(9):
    teste += digitos[i] * (10 - i)

if((teste % 11) < 2):
    teste = 0

else:
    teste = 11 - (teste % 11)

if(digitos[9] == teste):
    teste = 0

    for i in range(0,10):
        teste += digitos[i] * (11 - i)

    if((teste % 11) < 2):
        teste = 0
    else:
        teste = 11 - (teste % 11)

    if((digitos[10]) != teste):
        isCorreto = False

else:
    isCorreto = False

# Saida de dados
if(isCorreto):
    print("Este é um CPF válido!!!")
    print("A região fiscal em que foi emitido é:", DescobreRegiao(digitos[8]))

else:
    print("Este não é um CPF válido!!!")

# FIXME Ainda é possível digitar 12, e 13 numeros e ele ser valido
# FIXME Se digitar menos números ele para o código