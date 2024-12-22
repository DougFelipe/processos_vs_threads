# Matrix Multiplication: Sequential, Threaded, and Process-Based Implementations

This repository contains Python implementations of matrix multiplication using various approaches:
- Sequential
- Multi-threaded
- Multi-process

Each method is designed to calculate the product of two matrices, highlighting the differences in execution time and scalability as matrix size increases. The project is structured as follows:

## Project Structure

```
├── 1 Auxiliar
│   └── auxiliar.py          # Generates random matrices for multiplication
├── 2 Sequencial
│   └── sequencial.py        # Sequential matrix multiplication
├── 3 Paralelo Threads
│   └── threads.py           # Parallel matrix multiplication using threads
├── 4 Paralelo Processos
│   └── processos2.py        # Parallel matrix multiplication using processes
├── E1
│   ├── processos
│   │   ├── e1_processos.py  # Benchmark for process-based multiplication
│   │   └── matrix_multiplication_times.png
│   ├── sequencial
│   │   ├── e1_sequencial.py # Benchmark for sequential multiplication
│   │   └── resultado.png
│   └── threads
│       ├── e1_threads.py    # Benchmark for thread-based multiplication
│       └── resultado_threads.png
├── E2
│   ├── processos
│   │   ├── e2_processos2.py # Large matrix benchmark for process-based multiplication
│   │   ├── matrix_multiplication_times_process.png
│   │   └── results.xlsx
│   └── threads
│       ├── e2_threads.py    # Large matrix benchmark for thread-based multiplication
│       ├── matrix_multiplication_times_threads.png
│       └── results.xlsx
├── README.md                # Project documentation
├── Trabalho_Unidade_1.pdf   # Assignment description (in Portuguese)
└── auxiliar.py              # Script to generate random matrices
```

## Usage Instructions

### 1. Generating Matrices
The `auxiliar.py` script generates two random matrices and saves them to `M1.txt` and `M2.txt`.

#### Example:
```bash
python auxiliar.py <n1> <m1> <n2> <m2>
```
- `<n1>`, `<m1>`: Dimensions of matrix `M1`.
- `<n2>`, `<m2>`: Dimensions of matrix `M2`. Ensure `m1 == n2` for valid multiplication.

### 2. Sequential Multiplication
Use the `sequencial.py` script for a single-threaded matrix multiplication.

#### Example:
```bash
python 2\ Sequencial/sequencial.py
```
This will read `M1.txt` and `M2.txt` and output the product in `.txt` files with execution time included.

### 3. Parallel Multiplication Using Threads
The `threads.py` script distributes rows of `M1` across multiple threads for parallel computation.

#### Example:
```bash
python 3\ Paralelo\ Threads/threads.py <P>
```
- `<P>`: Number of rows assigned to each thread.

### 4. Parallel Multiplication Using Processes
The `processos2.py` script divides the workload across multiple processes using Python's multiprocessing library.

#### Example:
```bash
python 4\ Paralelo\ Processos/processos2.py <P>
```
- `<P>`: Number of rows assigned to each process.

## Benchmarks

The `E1` and `E2` directories provide benchmarks and visualizations of execution time for increasing matrix sizes. These experiments highlight the performance of sequential, threaded, and process-based methods.

### Graphs
- **Sequential Performance**: `E1/sequencial/resultado.png`
- **Thread-Based Performance**: `E1/threads/resultado_threads.png`
- **Process-Based Performance**: `E1/processos/matrix_multiplication_times.png`

### Results
For large-scale tests, refer to the `E2` directory, which includes:
- Execution time graphs
- Comparison tables in `results.xlsx`

## Requirements

- Python 3.8+
- Required libraries:
  - `numpy`
  - `matplotlib`
  - `argparse`
- Multiprocessing supported by the system

### Install Dependencies
Install dependencies using pip:
```bash
pip install numpy matplotlib
```

## Contributions

Feel free to contribute by submitting a pull request or reporting issues.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
