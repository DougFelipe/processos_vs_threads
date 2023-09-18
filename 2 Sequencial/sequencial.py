import numpy as np
import time


def sequencial(file1, file2):
    # Carregar matrizes dos arquivos
    M1 = np.loadtxt(file1, dtype=int)
    M2 = np.loadtxt(file2, dtype=int)
    
    # Verificar dimensões para multiplicação
    if M1.shape[1] != M2.shape[0]:
        raise ValueError("m1 deve ser igual a n2.")
    
    # Multiplicação de matrizes calculando os tempos inicial e finl
    start_time = time.time()
    result = np.dot(M1, M2)
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    
    # nomes dos arquivos de saída
    output_file_1 = file1.replace(".txt", "_seq_calc.txt")
    output_file_2 = file2.replace(".txt", "_seq_calc.txt")
    
    # Salvar resultado no arquivo 1
    with open(output_file_1, "w") as f:
        # Escreve dimensões 
        f.write(f"{result.shape[0]} {result.shape[1]}\n")
        
        # Escreve matriz resultante com coordenadas
        for i in range(result.shape[0]):
            for j in range(result.shape[1]):
                f.write(f"{i+1}{j+1} {result[i, j]}\n")
        
        # Escrever tempo de execução
        f.write(f"{elapsed_time:.6f}\n")
    
    # Copiar arquivo 1 para arquivo 2
    with open(output_file_2, "w") as f:
        f.write(open(output_file_1).read())
    
    return output_file_1, output_file_2

# testando com o output de auxiliar.py
output_files = sequencial("/mnt/d/Tecnologia da Informação (TI)/P4 2023.2/Sistemas Operacionais/Trabalho Unidade I/2 Sequencial/M1.txt", "/mnt/d/Tecnologia da Informação (TI)/P4 2023.2/Sistemas Operacionais/Trabalho Unidade I/2 Sequencial/M2.txt")
