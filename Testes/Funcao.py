import matplotlib.pyplot as plt  # type: ignore 
import numpy as np  # type: ignore
import tkinter as tk
from tkinter import simpledialog, messagebox


# Janela principal invisível com tamanho semelhante à janela do gráfico
root = tk.Tk()
root.geometry("800x600")
root.withdraw()

def readFloat(msg):
    while True:
        try:
            valor = simpledialog.askfloat("Entrada de Dados", msg, parent=root)
            if valor is None:
                raise ValueError("Cancelado")
            return valor
        except:
            messagebox.showerror("Erro", "Digite um número válido.", parent=root)

# Entradas
b = readFloat("Número inicial de células:")
a = readFloat("Taxa de crescimento exponencial (ex: 1.03 para 3%):")
taxaLinear = readFloat("Taxa de crescimento linear (por dia):")
tempoFinal = readFloat("Tempo final da simulação (dias):")

# Vetor de tempo
x = np.linspace(0, tempoFinal, 100)

# ======== GRÁFICO 1: ANTES DO TRATAMENTO ========
yCancer = b * (a ** x)
yNormal = b + taxaLinear * x

plt.figure("Antes do Tratamento", figsize=(8, 6))
plt.plot(x, yCancer, label="Células Cancerígenas (Exponencial)", color="red")
plt.plot(x, yNormal, label="Células Normais (Linear)", color="green")
plt.xlabel("Tempo (dias)")
plt.ylabel("Número de células")
plt.title("Antes do Tratamento")
plt.legend()
plt.grid(True)

dados = f"""Células iniciais: {b}
Taxa exponencial: {a}
Taxa linear: {taxaLinear}
Tempo total: {tempoFinal} dias"""

plt.annotate(dados,
             xy=(tempoFinal * 0.7, max(max(yCancer), max(yNormal)) * 0.6),
             fontsize=10,
             bbox=dict(boxstyle="round", facecolor='white', alpha=0.7))

# Escala log?
usar_log = messagebox.askyesno("Escala logarítmica", "Usar escala logarítmica no eixo Y?", parent=root)
if usar_log:
    plt.yscale("log")

# ======== GRÁFICO 2: APÓS O TRATAMENTO ========
# Simulação de tratamento:
a_tratado = a * 0.8  # Reduz crescimento exponencial
taxaLinear_tratado = taxaLinear * 0.95  # Leve impacto nas normais

yCancerTratado = b * (a_tratado ** x)
yNormalTratado = b + taxaLinear_tratado * x

plt.figure("Após o Tratamento", figsize=(8, 6))
plt.plot(x, yCancerTratado, label="Câncer (Tratado)", color="orange")
plt.plot(x, yNormalTratado, label="Normais (Tratamento)", color="blue")
plt.xlabel("Tempo (dias)")
plt.ylabel("Número de células")
plt.title("Após o Tratamento")
plt.legend()
plt.grid(True)

dados_tratado = f"""TRATAMENTO:
Nova taxa cancerígena: {round(a_tratado, 4)}
Nova taxa linear: {round(taxaLinear_tratado, 4)}"""

plt.annotate(dados_tratado,
             xy=(tempoFinal * 0.7, max(max(yCancerTratado), max(yNormalTratado)) * 0.6),
             fontsize=10,
             bbox=dict(boxstyle="round", facecolor='white', alpha=0.7))

if usar_log:
    plt.yscale("log")

plt.tight_layout()
plt.show()
