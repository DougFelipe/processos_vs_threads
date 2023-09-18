import numpy as np
import time
import os
import multiprocessing
import matplotlib.pyplot as plt
from multiprocessing import Pool

# Funções do auxiliar.py
def generate_matrices(n1, m1, n2, m2):
    M1 = np.random.randint(0, 10, size=(n1, m1))
    M2 = np.random.randint(0, 10, size=(n2, m2))
    return M1, M2

# Funções do processos.py
def processos(args):
    segment_index, M1_segment, M2, P, output_file_prefix = args
    local_start_time = time.time()
    result_segment = np.dot(M1_segment, M2)
    elapsed_time = time.time() - local_start_time
    return segment_index, result_segment, elapsed_time

def multiplicação_processos(P, M1, M2):
    n1, m1 = M1.shape
    n2, m2 = M2.shape
    total_elements = n1 * m2
    total_segments = -(-total_elements // P)
    output_file_prefix = os.path.join(os.getcwd(), "output_process_pooling")

    with Pool(processes=multiprocessing.cpu_count()) as pool:
        args = [(i, M1[i * P:(i + 1) * P], M2, P, output_file_prefix) for i in range(total_segments)]
        results = pool.map(processos, args)

    # Reorganizar os resultados em uma matriz única
    sorted_results = sorted(results, key=lambda x: x[0])
    result_matrix = np.vstack([result[1] for result in sorted_results])

    return result_matrix

# Script principal calculando com o valor para 2 min
def main():
    n1 = m1 = n2 = m2 = 2150  # Tamanho da matriz
    P = 2  # Número de processos

    # Gerar as matrizes uma vez no início
    M1, M2 = generate_matrices(n1, m1, n2, m2)

    times = []
    sizes = []

    while True:
        total_time = 0
        for _ in range(10):
            start_time = time.time()
            result_matrix = multiplicação_processos(P, M1, M2)
            total_time += time.time() - start_time

        average_time = total_time / 10
        sizes.append(n1)
        times.append(average_time)

        print(f"Tempo Médio para Matriz de {n1}x{n1} com {P} processos: {average_time:.6f} segundos")

        if average_time >= 120:
            break

        n1 = m1 = n2 = m2 = n1 * 2

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, marker='o', linestyle='-')
    plt.xlabel('Tamanho da Matriz')
    plt.ylabel('Tempo Médio (s)')
    plt.title('Tempo Médio x Tamanho da Matriz')
    plt.grid(True)
    plt.savefig("matrix_multiplication_times.png")

if __name__ == "__main__":
    main()
