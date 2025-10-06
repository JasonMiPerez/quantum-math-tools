# Singular Value Decomposition (CLI Tool)

A lightweight Python command-line program to compute the **Singular Value Decomposition (SVD)** of a user-provided matrix.  
The program takes matrix dimensions and entries as input, then prints the matrices **U**, **Σ**, and **Vᵀ**.

---

## 🛠️ Requirements
- Python 3.9+
- NumPy

---

## 🚀 Run
From this folder:
```bash
python SVD.py
```
You will be prompted to enter:
1. Two integers m n (matrix dimensions)
2. The m × n matrix entries (row by row)

The program will output the decomposition:
- U (left singular vectors)
- Σ (singular values)
- Vᵀ (right singular vectors)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE)
