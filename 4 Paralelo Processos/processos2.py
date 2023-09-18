import numpy as np
import time
import os
import argparse
import multiprocessing

from multiprocessing import Pool

# Função para calcular um segmento da matriz por processos 
def processos(segment_index, M1, M2, P, output_file_prefix):
    start_index = segment_index * P
    end_index = min((segment_index + 1) * P, M1.shape[0])
    
    # Inicia a contagem do tempo
    local_start_time = time.time()
    
    # Calcula o segmento da matriz
    result_segment = np.dot(M1[start_index:end_index], M2)
    
    # Grava o segmento em um arquivo
    output_file = f"{output_file_prefix}_{segment_index}.txt"
    with open(output_file, "w") as f:
        # Escreve dimensões da matriz total
        f.write(f"{M1.shape[0]} {M2.shape[1]}\n")
        
        # Escreve o segmento da matriz
        for i in range(result_segment.shape[0]):
            for j in range(result_segment.shape[1]):
                f.write(f"{start_index + i + 1}{j + 1} {result_segment[i, j]}\n")
        
        # Escreve tempo de execução
        elapsed_time = time.time() - local_start_time
        f.write(f"{elapsed_time:.6f}\n")
    
    return output_file

def multiplicação_processos(P):
    # diretório atual do script
    current_directory = os.path.dirname(os.path.abspath(__file__))
    
    # caminhos para os arquivos M1 e M2
    file1 = os.path.join(current_directory, "M1.txt")
    file2 = os.path.join(current_directory, "M2.txt")
    
    # faz o load das matrizes dos arquivos
    M1 = np.loadtxt(file1, dtype=int)
    M2 = np.loadtxt(file2, dtype=int)
    
    # número total de segmentos
    n1, m1 = M1.shape
    n2, m2 = M2.shape
    total_elements = n1 * m2
    total_segments = -(-total_elements // P) 
    
    # arquivo de saída com base no diretório atual
    output_file_prefix = os.path.join(current_directory, "output_process_pooling")
    
    # calcular os segmentos em paralelo
    with Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.starmap(processos, [(i, M1, M2, P, output_file_prefix) for i in range(total_segments)])
    
    return results

if __name__ == "__main__":
    # inserindo o valor de P da linha de comando
    parser = argparse.ArgumentParser(description="multiplicação de matrizes em paralelo usando processos.")
    parser.add_argument("P", type=int)
    args = parser.parse_args()
    
    output_files_process = multiplicação_processos(args.P)
    print(output_files_process)
