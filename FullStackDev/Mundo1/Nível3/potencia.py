# script potencia.py
def calcula_potencia(expoente):
    def potencia(base):
        return base**expoente

    return potencia


# parte principal do programa
def main():
    base_expoente = input()
    # separa base e expoente, convertendo-os para inteiros
    base, expoente = (int(i) for i in base_expoente.split())

    # utilizando a função calcula_potencia
    potencia_de = calcula_potencia(expoente)
    res_potencia = potencia_de(base)
    print(f"{base} elevado a {expoente} = {res_potencia}")


if __name__ == "__main__":
    main()
