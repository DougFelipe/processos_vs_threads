import numpy as np
import time
import threading
import os
import matplotlib.pyplot as plt

# Função generate_matrices de auxiliar.py
def gerar_matriz_auxiliar(n1, m1, n2, m2):
    M1 = np.random.randint(0, 10, size=(n1, m1))
    M2 = np.random.randint(0, 10, size=(n2, m2))
    
    np.savetxt("M1.txt", M1, fmt='%d')
    np.savetxt("M2.txt", M2, fmt='%d')
    print("Matrizes salvas em M1.txt e M2.txt")

# Função compute_matrix_segment de threads.py
def matriz_threads(start_row, end_row, M1, M2, output_file_prefix, segment_index):
    local_start_time = time.time()
    
    result_segment = np.dot(M1[start_row:end_row], M2)
    output_file = f"{output_file_prefix}_{segment_index}.txt"
    
    with open(output_file, "w") as f:
        f.write(f"{M1.shape[0]} {M2.shape[1]}\n")
        
        for i in range(result_segment.shape[0]):
            for j in range(result_segment.shape[1]):
                f.write(f"{start_row + i + 1}{j + 1} {result_segment[i, j]}\n")
        f.write(f"{time.time() - local_start_time:.6f}\n")

# Função threads de threads.py
def threads(P):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file1 = os.path.join(current_directory, "M1.txt")
    file2 = os.path.join(current_directory, "M2.txt")
    
    M1 = np.loadtxt(file1, dtype=int)
    M2 = np.loadtxt(file2, dtype=int)
    
    total_threads = -(-M1.shape[0] // P)
    
    threads = []
    for i in range(total_threads):
        start_row = i * P
        end_row = min((i + 1) * P, M1.shape[0])
        output_file_prefix = os.path.join(current_directory, "output")
        
        thread = threading.Thread(target=matriz_threads, args=(start_row, end_row, M1, M2, output_file_prefix, i))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    return [f"output_{i}.txt" for i in range(total_threads)]

# Script principal calculando com o valor para 2 min
def main():
    size = 2150  # Tamanho da matriz
    P = 2  # Número de threads
    
    gerar_matriz_auxiliar(size, size, size, size)
    
    total_time = 0
    for _ in range(10):
        start_time = time.time()
        threads(P)
        total_time += time.time() - start_time
    average_time = total_time / 10
    
    print(f"Tempo Médio para Matriz de {size}x{size} com {P} threads: {average_time:.6f} segundos")

if __name__ == "__main__": 
    main()
