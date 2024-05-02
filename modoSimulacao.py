import random
import numpy as np




def modSim():
    print("========= Modo Simulação Ativado ========")

    print("**** Solicitações User 1 - Aleatório *****")
    for _ in range(200):
        solicitarUserAleatorio()

    print("**** Solicitação User 2 - Probabilidade *****")
    for _ in range(200):
        solicitarUserChance()

    print("**** Solicitação User 3 - Poisson *****")
    for _ in range(200):
        solicitarUserPoisson()

def solicitarUserAleatorio():
    numeroArquivo = random.randint(1, 100)
    print(numeroArquivo)
    return numeroArquivo

def solicitarUserChance():
    numeros_especiais = [num for num in range(30, 41) for _ in range(33)]
    numeros_restantes = [num for num in range(1, 101) if num not in numeros_especiais]
    numero_arquivo = random.choice(numeros_especiais + numeros_restantes)
    print(numero_arquivo)
    return numero_arquivo

def solicitarUserPoisson():
    lambd = 40
    numeroArquivo3 = np.random.poisson(lam=lambd, size=1)
    print(numeroArquivo3)
    return numeroArquivo3[0]



def solicitarUserChance():
  # Criar uma lista com 33 ocorrências dos números entre 30 e 40
  numeros_especiais = [num for num in range(30, 41) for _ in range(33)]

  # Preencher o restante da lista com os números de 1 a 100
  numeros_restantes = [
    num for num in range(1, 101) if num not in numeros_especiais
  ]

  # Escolher aleatoriamente um número dessa lista expandida
  numero_arquivo = random.choice(numeros_especiais + numeros_restantes)

  print(numero_arquivo)
  return numero_arquivo


def solicitarUserPoisson():
  lambd = 40  # lambda para a distribuição de Poisson
  numeroArquivo3 = np.random.poisson(lam=lambd, size=1)

  print(numeroArquivo3)
  return numeroArquivo3[0]
