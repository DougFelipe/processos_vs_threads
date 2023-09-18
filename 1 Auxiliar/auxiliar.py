import numpy as np
import sys

def gerar_matriz_auxiliar(n1, m1, n2, m2):
    # Verificar se a multiplicação de matrizes é possível
    if m1 != n2:
        raise ValueError("m1 deve ser igual a n2.")
    
    # Gerar matrizes 
    M1 = np.random.randint(0, 10, size=(n1, m1)) 
    M2 = np.random.randint(0, 10, size=(n2, m2))
    
    # Salvar matrizes
    np.savetxt("M1.txt", M1, fmt='%d')
    np.savetxt("M2.txt", M2, fmt='%d')
    
if __name__ == "__main__":
        
    n1, m1, n2, m2 = map(int, sys.argv[1:])
    gerar_matriz_auxiliar(n1, m1, n2, m2)
