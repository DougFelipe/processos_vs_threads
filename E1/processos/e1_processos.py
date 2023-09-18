import numpy as np
import time
import os
import multiprocessing
import matplotlib.pyplot as plt
from multiprocessing import Pool

# Funções do auxiliar.py
def gerar_matriz_auxiliar(n1, m1, n2, m2):
    M1 = np.random.randint(0, 10, size=(n1, m1))
    M2 = np.random.randint(0, 10, size=(n2, m2))
    np.savetxt("M1.txt", M1, fmt='%d')
    np.savetxt("M2.txt", M2, fmt='%d')
    print("Matrizes salvas em M1.txt e M2.txt")

# Funções do processos.py
def processos(segment_index, M1, M2, P, output_file_prefix):
    start_index = segment_index * P
    end_index = min((segment_index + 1) * P, M1.shape[0])
    local_start_time = time.time()
    result_segment = np.dot(M1[start_index:end_index], M2)
    output_file = f"{output_file_prefix}_{segment_index}.txt"
    with open(output_file, "w") as f:
        f.write(f"{M1.shape[0]} {M2.shape[1]}\n")
        for i in range(result_segment.shape[0]):
            for j in range(result_segment.shape[1]):
                f.write(f"{start_index + i + 1}{j + 1} {result_segment[i, j]}\n")
        elapsed_time = time.time() - local_start_time
        f.write(f"{elapsed_time:.6f}\n")
    return output_file

def multiplicação_processos(P):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file1 = os.path.join(current_directory, "M1.txt")
    file2 = os.path.join(current_directory, "M2.txt")
    M1 = np.loadtxt(file1, dtype=int)
    M2 = np.loadtxt(file2, dtype=int)
    if M1.shape[1] != M2.shape[0]:
        raise ValueError("As dimensões das matrizes não permitem multiplicação.")
    n1, m1 = M1.shape
    n2, m2 = M2.shape
    total_elements = n1 * m2
    total_segments = -(-total_elements // P)
    output_file_prefix = os.path.join(current_directory, "output_process_pooling")
    with Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.starmap(processos, [(i, M1, M2, P, output_file_prefix) for i in range(total_segments)])
    return results

# Script principal pra calcular com o incremnto de 2x no tamanho da matriz
def main():
    n1 = m1 = n2 = m2 = 100
    times = []
    sizes = []
    
    while True:
        gerar_matriz_auxiliar(n1, m1, n2, m2)
        P = (n1 * m2) // 8
        total_time = 0
        for _ in range(10):
            start_time = time.time()
            multiplicação_processos(P)
            total_time += time.time() - start_time
        average_time = total_time / 10
        sizes.append(n1)
        times.append(average_time)
        if average_time >= 120:
            break
        n1 = m1 = n2 = m2 = n1 * 2

    plt.figure(figsize=(10,6))
    plt.plot(sizes, times, marker='o', linestyle='-')
    plt.xlabel('Tamanho da Matriz')
    plt.ylabel('Tempo Médio (s)')
    plt.title('Tempo Médio x Tamanho da Matriz')
    plt.grid(True)
    plt.savefig("matrix_multiplication_times.png")

if __name__ == "__main__":
    main()
