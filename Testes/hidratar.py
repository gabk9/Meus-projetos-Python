import time, msvcrt, os, json, winsound
from datetime import datetime, timedelta, date

tittle = "Hidrate-se"
ARQUIVO = "Hidrate-se.json"
USER_DATA = "Hidrate-se_Userdata.json"

def Sleep(ms):
    time.sleep(ms / 1000)

def type(text, ms):
    for i in range(len(text)):
        print(text[i], end="", flush=True)
        Sleep(ms)

def cls():
    os.system('cls')

def pause():
    print("Pressione qualquer tecla para continuar...")
    msvcrt.getch()

def Vload(ms):
    bar = 30
    for i in range(bar + 1):
        percent = (i * 100) / bar
        print("\r[", end="", flush=True)
        print("#"*i, end="", flush=True)
        print(" "*(bar-i), end="", flush=True)
        print(f"] {percent:3.0f}%", end="", flush=True)
        Sleep(ms)
    print()

def regist():
    cls()
    errorCount = None
    while errorCount != 0:
        errorCount = 0
        try:
            print(f"{tittle:=^25}")
            name = input("Me diga seu nome: ")
            sex = input("Me diga seu sexo (M/F): ").upper()
            age = int(input("Me diga sua idade: "))
            activity = input("Qual é a frequência de atividade física (M - 3 a 5 dias / A - 5 a 7 dias / S - Sedentário): ").upper()
            weight = float(input("Me diga seu peso: "))
        except ValueError:
            print("Valor inválido!!")
            pause()
            cls()
            errorCount += 1

    user = {
        "Nome": name,
        "Sexo": sex,
        "Idade": age,
        "Frequência": activity,
        "Peso": weight
    }

    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(user, f, indent=4, ensure_ascii=False)
        print("Dados salvos com sucesso!!")
        pause()
        cls()

def alarmConfig():
    cls()
    typeSpeed = 7
    while True:
        print(f"{tittle:=^25}")
        type("Que horas que você acorda? (HH:MM) ", typeSpeed)
        init_hours = input()
        if not valError(init_hours):
            pause()
            cls()
            continue

        type("Que horas que você dorme? (HH:MM) ", typeSpeed)
        end_hours = input()
        if not valError(end_hours):
            pause()
            cls()
            continue

        break

    config = {
        "Acorda": init_hours,
        "Dorme": end_hours
    }

    with open(USER_DATA, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)
        print("Dados salvos com sucesso!!")
        pause()
        cls()

def valError(hours_str):
    try:
        datetime.strptime(hours_str, "%H:%M").time()
        return True
    except ValueError:
        print("Formato inválido! Use HH:MM (ex: 14:30)")
        return False

def AlarmMenu():
    cls()
    try:
        with open(USER_DATA, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                Vload(15)
                alarmConfig()
    except FileNotFoundError:
        Vload(15)
        alarmConfig()

    with open(ARQUIVO, "r", encoding="utf-8") as f:
        user = json.load(f)
    with open(USER_DATA, "r", encoding="utf-8") as f:
        config = json.load(f)

    weight = user["Peso"]
    age = user["Idade"]
    gender = user["Sexo"]
    activity = user["Frequência"]

    wake_time = datetime.strptime(config["Acorda"], "%H:%M")
    sleep_time = datetime.strptime(config["Dorme"], "%H:%M")
    today = datetime.today()
    wake_time = wake_time.replace(year=today.year, month=today.month, day=today.day)
    sleep_time = sleep_time.replace(year=today.year, month=today.month, day=today.day)
    if sleep_time <= wake_time:
        sleep_time += timedelta(days=1)

    water_per_kg = 35
    match activity:
        case "M":
            water_per_kg = 40
        case "A":
            water_per_kg = 45
        case "S":
            water_per_kg = 30

    if gender == "M" and age < 30:
        water_per_kg += 2
    elif gender == "F" and age < 30:
        water_per_kg += 1

    total_water = weight * water_per_kg
    interval_min = 60
    active_hours = int((sleep_time - wake_time).total_seconds() // 3600)
    doses = active_hours
    water_per_dose = total_water / doses

    cls()
    print(f"{tittle:=^25}")
    print(f"Voce deveria beber aproximadamente {total_water:.0f} ml de água hoje.")
    print(f"Vai ter {doses} alarmes a cada {interval_min} minutos (~{water_per_dose:.0f} ml por dose).")
    Sleep(3000)
    cls()

    now = datetime.now().replace(second=0, microsecond=0)
    next_alarm = wake_time
    while next_alarm <= now:
        next_alarm += timedelta(hours=1)

    while next_alarm < sleep_time:
        now = datetime.now()
        if next_alarm > now:
            delta_seconds = (next_alarm - now).total_seconds()
            time.sleep(delta_seconds)
        message = f"[{next_alarm.strftime('%H:%M')}] Hora de tomar {water_per_dose:.0f} ml de água!"
        print(f"\r{message}{' ' * (50 - len(message))}", end="", flush=True)
        winsound.Beep(500, 1000)
        next_alarm += timedelta(hours=1)

    print("\nVocê tomou toda a água de hoje!!")
    pause()
    cls()

def EditMenu():
    cls()
    typeSpeed = 7
    while True:
        print(f"{tittle:=^25}")
        type("[1] Editar horários\n[2] editar dados do usuário\n[0] Voltar\n", typeSpeed)
        typeSpeed = 0
        try:
            op = int(input("Escolha uma opção: "))

        except ValueError:
            print("Valor inválido!!")
            pause()
            cls()

        match op:
            case 1:
                regist()
            case 2:
                alarmConfig()
            case 0:
                pause()
                cls()
                break
            case _:
                print("Opção inválida!!")
                pause()
                cls()

def main():
    typeSpeed = 7
    Vload(25)
    cls()

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                print("Arquivo vazio! Entrando no menu de registrar...")
                Vload(15)
                regist()

    except FileNotFoundError:
        print(f"{tittle:=^25}")
        print("Entrando no menu de registrar...")
        Vload(15)
        regist()

    while True:
        print(f"{tittle:=^25}")
        type("[1] Iniciar Alarme\n[2] Editar dados\n[0] Sair", typeSpeed)
        typeSpeed = 0
        try:
            op = int(input("\nEscolha uma opção: "))

        except ValueError:
            print("Valor inválido!!")
            pause()
            cls()
            continue

        match op:
            case 1:
                AlarmMenu()
            case 2:
                EditMenu()
            case 0:
                print("Encerrando o programa...")
                break
            case _:
                print("Opção inválida!!")
                pause()
                cls()

if __name__ == "__main__":
    main()
