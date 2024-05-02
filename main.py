from lru import Lru
from lfu import Lfu
from fifo import Fifo
import modoSimulacao as ms  # Importe o módulo modoSimulacao
import separaArquivos as sa  # Importe o módulo separaArquivos
import random
import os

def print_resultados(algoritmo, cache_misses, cache_hits, tempos_medios):
    print(f"{algoritmo}:")
    print("  Cache Misses   Cache Hits   Tempo Médio")
    for i in range(3):
        print(f"  {cache_misses[i]:<14} {cache_hits[i]:<12} {tempos_medios[i]:<18}")

def determinar_melhor_algoritmo(fifo_hits, lru_hits, lfu_hits):
    melhor_algoritmo = max({'FIFO': fifo_hits, 'LRU': lru_hits, 'LFU': lfu_hits}, key=lambda x: x[1])
    return melhor_algoritmo

def gerar_relatorio(cache_misses, cache_hits, tempos_medios, melhor_algoritmo):
    with open("relatorio.txt", "w") as file:
        file.write("As médias de tempo cache hit and time:\n")
        file.write(f"User 1: {tempos_medios[0]}\n")
        file.write(f"User 2: {tempos_medios[1]}\n")
        file.write(f"User 3: {tempos_medios[2]}\n\n")
        file.write("A quantidade de Cache Miss em cada user:\n")
        file.write(f"User 1: {cache_misses[0]}\n")
        file.write(f"User 2: {cache_misses[1]}\n")
        file.write(f"User 3: {cache_misses[2]}\n\n")
        file.write("A quantidade de arquivos que já estavam no cache:\n")
        file.write(f"User 1: {cache_hits[0]}\n")
        file.write(f"User 2: {cache_hits[1]}\n")
        file.write(f"User 3: {cache_hits[2]}\n\n")
        file.write("RESULTADOS DA SIMULAÇÃO:\n")
        file.write("----------------------------------------\n")
        file.write("\n")
        file.write("FIFO:\n")
        file.write("  Cache Misses   Cache Hits   Tempo Médio\n")
        for i in range(3):
            file.write(f"  {cache_misses[0][i]:<14} {cache_hits[0][i]:<12} {tempos_medios[0][i]:<18}\n")
        file.write("\n")
        file.write("LFU:\n")
        file.write("  Cache Misses   Cache Hits   Tempo Médio\n")
        for i in range(3):
            file.write(f"  {cache_misses[1][i]:<14} {cache_hits[1][i]:<12} {tempos_medios[1][i]:<18}\n")
        file.write("\n")
        file.write("LRU:\n")
        file.write("  Cache Misses   Cache Hits   Tempo Médio\n")
        for i in range(3):
            file.write(f"  {cache_misses[2][i]:<14} {cache_hits[2][i]:<12} {tempos_medios[2][i]:<18}\n")
        file.write("\n")
        file.write(f"Melhor algoritmo de cache: {melhor_algoritmo}\n")

def executar_simulacao():
    # Instancie os objetos para cada algoritmo de cache
    fifo = Fifo()
    lfu = Lfu()
    lru = Lru()

    # Realize a simulação para cada algoritmo de cache
    miss_fifo, found_fifo, tempo_fifo = fifo.simulacao()
    miss_lfu, found_lfu, tempo_lfu = lfu.simulacao()
    miss_lru, found_lru, tempo_lru = lru.simulacao()

    # Apresente os resultados da simulação
    print("\nRESULTADOS DA SIMULAÇÃO:")
    print_resultados("FIFO", miss_fifo, found_fifo, tempo_fifo)
    print_resultados("LFU", miss_lfu, found_lfu, tempo_lfu)
    print_resultados("LRU", miss_lru, found_lru, tempo_lru)

    # Determine o melhor algoritmo de cache
    melhor_algoritmo = determinar_melhor_algoritmo(
        sum(found_fifo), sum(found_lfu), sum(found_lru)
    )
    print(f"Melhor algoritmo de cache: {melhor_algoritmo}")

    # Gerar relatório
    gerar_relatorio([miss_fifo, miss_lfu, miss_lru], [found_fifo, found_lfu, found_lru], [tempo_fifo, tempo_lfu, tempo_lru], melhor_algoritmo)

def ler_arquivo():
    while True:
        arquivo_selecionado = input("Digite o número do arquivo que deseja ler, ou -1 para iniciar o modo simulação (ou 'sair' para encerrar): ")
        if arquivo_selecionado.lower() == 'sair':
            print("Programa encerrado.")
            return False
        elif arquivo_selecionado == '-1':
            print("Iniciando modo simulação...")
            executar_simulacao()  # Chame a função de simulação
            continue
        else:
            # Construir o caminho completo para o arquivo
            caminho_arquivo = os.path.join(diretorio_atual, "arquivos_divididos", f"arquivo_{arquivo_selecionado}.txt")
            # Verificar se o arquivo existe
            if os.path.exists(caminho_arquivo):
                # Ler e exibir o conteúdo do arquivo
                print(f"\nLendo o arquivo 'arquivo_{arquivo_selecionado}.txt'...")
                with open(caminho_arquivo, 'r') as arquivo:
                    conteudo = arquivo.read()
                    print(conteudo)
            else:
                print("Arquivo não encontrado.")
                continue

# Início do programa
print("Arquivos sendo divididos...")
sa.sepArquivos()
fifo = Fifo()
lfu = Lfu()
lru = Lru()

# Obter o caminho absoluto do diretório atual
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Permitindo que o usuário selecione um arquivo para ler
while True:
    print("\nMENU:")
    print("1. Ler arquivo")
    print("-1. Iniciar modo simulação")
    print("3. Encerrar programa")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        ler_arquivo()
    elif escolha == '-1':
        print("Iniciando modo simulação...")
        executar_simulacao()
    elif escolha == '3':
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
