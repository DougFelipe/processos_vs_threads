import numpy as np
import time
import matplotlib.pyplot as plt

# Funções auxiliares e sequenciais já fornecidas
def gerar_matriz_auxiliar(n1, m1, n2, m2):
    
    M1 = np.random.randint(0, 10, size=(n1, m1))
    M2 = np.random.randint(0, 10, size=(n2, m2))
    np.savetxt("M1.txt", M1, fmt='%d')
    np.savetxt("M2.txt", M2, fmt='%d')

def sequencial(file1, file2):
    M1 = np.loadtxt(file1, dtype=int)
    M2 = np.loadtxt(file2, dtype=int)
    
    
    start_time = time.time()
    result = np.dot(M1, M2)
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    output_file_1 = file1.replace(".txt", "_seq_calc.txt")
    output_file_2 = file2.replace(".txt", "_seq_calc.txt")
    
    with open(output_file_1, "w") as f:
        f.write(f"{result.shape[0]} {result.shape[1]}\n")
        for i in range(result.shape[0]):
            for j in range(result.shape[1]):
                f.write(f"{i+1}{j+1} {result[i, j]}\n")
        f.write(f"{elapsed_time:.6f}\n")
    
    with open(output_file_2, "w") as f:
        f.write(open(output_file_1).read())
    
    return elapsed_time

# Script principal pra calcular com o incremnto de 2x no tamanho da matriz
def main():
    size = 100
    times = []
    sizes = []
    
    while True:
        # Gera as matrizes
        gerar_matriz_auxiliar(size, size, size, size)
        
        # Calcula a multiplicação 10 vezes e obtém o tempo médio
        total_time = 0
        for _ in range(10):
            total_time += sequencial("M1.txt", "M2.txt")
        average_time = total_time / 10
        
        # Registra os resultados
        sizes.append(size)
        times.append(average_time)
        
        # Condição de parada
        if average_time >= 120:  # 2 minutos em segundos
            break
        
        # Dobra o tamanho da matriz para a próxima iteração
        size *= 2
    
    # Plotagem do gráfico
    plt.figure(figsize=(10,6))
    plt.plot(sizes, times, marker='o', linestyle='-')
    plt.xlabel('Tamanho da Matriz')
    plt.ylabel('Tempo Médio (s)')
    plt.title('Tempo Médio x Tamanho da Matriz')
    plt.grid(True)
    plt.savefig('resultado.png')  # Salva o gráfico como imagem


# Como estou em um ambiente isolado, você deve copiar e testar este código em sua máquina local
# Para executar, basta chamar a função main().


if __name__ == "__main__":
    main()
