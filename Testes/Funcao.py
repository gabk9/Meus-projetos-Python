def calculadora():
    print("Bem-vindo à calculadora! Digite 'sair' para encerrar, '=' para mostrar o resultado.\n")

    resultado = None

    while True:
        # Se resultado for None, pede o primeiro número
        if resultado is None:
            entrada = input("Digite o primeiro número (ou 'sair'): ")
            if entrada.lower() == "sair":
                break
            try:
                resultado = float(entrada)
            except ValueError:
                print("Número inválido! Tente novamente.")
                continue
        else:
            op = input("Digite a operação (+, -, *, /), '=' para mostrar resultado, ou 'sair': ").strip()
            if op == "=":
                print(f"Resultado atual: {resultado}")
                continue
            if op.lower() == "sair":
                break
            if op not in ["+", "-", "*", "/"]:
                print("Operação inválida! Tente novamente.")
                continue

            entrada = input("Digite o próximo número: ")
            try:
                num = float(entrada)
            except ValueError:
                print("Número inválido! Tente novamente.")
                continue

            if op == "+":
                resultado += num
            elif op == "-":
                resultado -= num
            elif op == "*":
                resultado *= num
            elif op == "/":
                if num == 0:
                    print("Erro: divisão por zero!")
                    continue
                resultado /= num

def main():
    calculadora()
    print("Até mais!")

if __name__ == "__main__":
    main()
