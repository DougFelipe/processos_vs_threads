import numpy as np
import threading
import time
import os
import argparse

# calcular um segmento da matriz resultante
def matriz_threads(start_row, end_row, M1, M2, output_file_prefix, segment_index):
    
    # contagem do tempo da thread
    local_start_time = time.time()
    
    # faz o segmento da matriz
    result_segment = np.dot(M1[start_row:end_row], M2)
    
    # savla o segmento em um arquivo
    output_file = f"{output_file_prefix}_{segment_index}.txt"
    with open(output_file, "w") as f:
        # dimensões da matriz total
        f.write(f"{M1.shape[0]} {M2.shape[1]}\n")
        
        # Escreve o segmento da matriz
        for i in range(result_segment.shape[0]):
            for j in range(result_segment.shape[1]):
                f.write(f"{start_row + i + 1}{j + 1} {result_segment[i, j]}\n")
        
        # calcula o tempo de execução
        f.write(f"{time.time() - local_start_time:.6f}\n")
 
def multiplica_threads(P):
    # diretório atual do script
    current_directory = os.path.dirname(os.path.abspath(__file__))
    
    # caminhos para os arquivos 
    file1 = os.path.join(current_directory, "M1.txt")
    file2 = os.path.join(current_directory, "M2.txt")
    
    # upload das matrizes dos arquivos
    M1 = np.loadtxt(file1, dtype=int)
    M2 = np.loadtxt(file2, dtype=int)
    
    
    # Calculando o número total de threads
    total_threads = -(-M1.shape[0] // P)  # Equivalent to ceil(M1.shape[0] / P)
    
    threads = []
    for i in range(total_threads):
        start_row = i * P
        end_row = min((i + 1) * P, M1.shape[0])
        
        # output do arquivo de saída com base no diretório atual
        output_file_prefix = os.path.join(current_directory, "output")
        
        thread = threading.Thread(target=matriz_threads, args=(start_row, end_row, M1, M2, output_file_prefix, i))
        threads.append(thread)
        thread.start()
    
    # esperando todas todas as threads terminarem para retornar os arquivos de saída
    for thread in threads:
        thread.join()
    
    return [f"output_{i}.txt" for i in range(total_threads)]

if __name__ == "__main__":
    # Configuração do argparse para aceitar o valor de P da linha de comando
    parser = argparse.ArgumentParser(description="multiplicação de matrizes em paralelo usando threads.")
    parser.add_argument("P", type=int)
    args = parser.parse_args()
    
    output_files = multiplica_threads(args.P)
    print(output_files)
