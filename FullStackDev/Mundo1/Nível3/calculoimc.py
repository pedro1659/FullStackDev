"Simples calculo de IMC"


def calculo_imc(peso_kg, altura_metros):
    """Calcula o IMC"""
    imc = peso_kg / altura_metros**2

    if imc < float(18.5):
        print("baixo peso")
    elif imc < float(24.9):
        print("peso adequado")
    elif imc < float(29.9):
        print("sobrepeso")
    else:
        print("obeso")


peso_str = input("Qual o seu peso?")
altura_str = input("Qual sua altura?")

# substituir a entrade do usuario com possiveis numeros com virgulas "," para ponto "."
peso = float(peso_str.replace(",", "."))
altura = float(altura_str.replace(",", "."))


calculo_imc(peso, altura)
