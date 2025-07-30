from simpleeval import simple_eval # type: ignore
import msvcrt, os

def cls():
    os.system('cls')

def pause(msg="Pressione qualquer tecla para continuar..."):
    print(msg)
    msvcrt.getch()

def main():
    while True:
        user_input = input('Insira uma expressão matemática, digite "sair" para sair": ').lower()
        if user_input == "sair":
            print("Saindo...\n")
            break
        try:
            result = simple_eval(user_input)
            print(float(result))
            pause()
            cls()
        except:
            print("Expressão inválida ou proibida.")
            pause()
            cls()
            
main()


# print(float(eval(input("Insira uma expressão matemática: ")))) 