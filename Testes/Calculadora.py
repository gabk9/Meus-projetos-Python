from simpleeval import simple_eval # type: ignore

user_input = input("Insira uma expressão matemática: ")
try:
    result = simple_eval(user_input)
    print(int(result))
except:
    print("Expressão inválida ou proibida.")


# print(float(eval(input("Insira uma expressão matemática: "))))