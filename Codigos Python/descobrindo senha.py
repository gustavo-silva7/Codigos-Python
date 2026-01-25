import tkinter as tk
import itertools
import string
import threading
import time

# ===== CONFIGURAÇÃO =====
SENHA_REAL = "guto1"
ALFABETO = string.ascii_lowercase + string.digits
TAMANHO_MAX = 3
DELAY = 0.01  # atraso só para visualização

# ===== FUNÇÃO QUE ABRE A TELA =====
def abrir_tela():
    tela = tk.Toplevel()
    tela.title("Sucesso")
    tk.Label(tela, text="Olá, mundo!", font=("Arial", 18)).pack(padx=40, pady=40)

# ===== FORÇA BRUTA =====
def quebrar_senha(status_label):
    tentativas = 0

    for tamanho in range(1, TAMANHO_MAX + 1):
        for combinacao in itertools.product(ALFABETO, repeat=tamanho):
            tentativa = "".join(combinacao)
            tentativas += 1

            status_label.config(
                text=f"Tentando: {tentativa} | Tentativas: {tentativas}"
            )
            time.sleep(DELAY)

            if tentativa == SENHA_REAL:
                status_label.config(
                    text=f"Senha encontrada: {tentativa} em {tentativas} tentativas"
                )
                abrir_tela()
                return

    status_label.config(text="Senha não encontrada")

# ===== INTERFACE =====
janela = tk.Tk()
janela.title("Demonstração de Força Bruta")

tk.Label(
    janela,
    text="Simulação de descoberta de senha (local)",
    font=("Arial", 12)
).pack(pady=10)

status = tk.Label(janela, text="Aguardando...", font=("Arial", 10))
status.pack(pady=10)

botao = tk.Button(
    janela,
    text="Iniciar",
    command=lambda: threading.Thread(
        target=quebrar_senha,
        args=(status,),
        daemon=True
    ).start()
)
botao.pack(pady=10)

janela.mainloop()



import itertools
import string
import time

SENHA_REAL = "guto2"
ALFABETO = string.ascii_lowercase + string.digits
TAMANHO_MAX = 8

tentativas = 0
inicio = time.time()

for tamanho in range(1, TAMANHO_MAX + 1):
    for combinacao in itertools.product(ALFABETO, repeat=tamanho):
        tentativa = "".join(combinacao)
        tentativas += 1

        print(f"Tentando: {tentativa}")

        if tentativa == SENHA_REAL:
            fim = time.time()
            print("\nSenha encontrada!")
            print("Senha:", tentativa)
            print("Tentativas:", tentativas)
            print(f"Tempo: {fim - inicio:.2f}s")
            exit()

print("Senha não encontrada")



SENHA_REAL = "guto1331314124"

def verifica_prefixo(tentativa):
    return SENHA_REAL.startswith(tentativa)

import string
import time

ALFABETO = string.ascii_lowercase + string.digits
TAMANHO_SENHA = len("guto1331314124")

senha_descoberta = ""
tentativas = 0
inicio = time.time()

for posicao in range(TAMANHO_SENHA):
    for char in ALFABETO:
        tentativas += 1
        tentativa = senha_descoberta + char

        print(f"Tentando: {tentativa}")

        if verifica_prefixo(tentativa):
            senha_descoberta += char
            print(f"✔ Caractere encontrado: {char}\n")
            break

fim = time.time()

print("Senha completa descoberta:", senha_descoberta)
print("Tentativas:", tentativas)
print(f"Tempo: {fim - inicio:.2f}s")




import string
import time
import sys

SENHA_REAL = "guto1123154353515142341gtesvfdvbb"
ALFABETO = string.ascii_lowercase + string.digits

def verifica_prefixo(tentativa):
    return SENHA_REAL.startswith(tentativa)

senha_descoberta = ""
tentativas = 0

print("Descobrindo senha: ", end="", flush=True)

for posicao in range(len(SENHA_REAL)):
    for char in ALFABETO:
        tentativas += 1
        tentativa = senha_descoberta + char

        # sobrescreve a mesma linha
        sys.stdout.write("\rDescobrindo senha: " + tentativa)
        sys.stdout.flush()
        time.sleep(0.05)  # só para visualização

        if verifica_prefixo(tentativa):
            senha_descoberta += char
            break

print(f"\n\nSenha encontrada: {senha_descoberta}")
print("Tentativas:", tentativas)
