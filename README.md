# Quantum Math Tools (Python CLI Programs)

A collection of small Python command-line tools created during quantum math research.  
Each script focuses on a different linear algebra or quantum-related computation, implemented in a lightweight and self-contained way.

---

## Included Tools

### 1. L1 Norm Approximation (`L1 Norm Approx.py`)
- Approximates a small complex matrix with a constrained rank-1 factorization.  
- Uses randomized search to minimize the **L1 norm error** under algebraic constraints.  
- Useful as a toy model for optimization and approximation methods.

### 2. Random Clifford Eigenvectors (`random_clifford_eigenvectors.py`)
- Generates random 1-qubit **Clifford operators** using Qiskit.  
- Extracts eigenvectors and maps them to the Bloch sphere (angles + Cartesian coordinates).  
- Produces scatter plots and 3D Bloch sphere visualizations of sampled eigenstates.

### 3. Singular Value Decomposition CLI (`SVD.py`)
- Simple CLI program to compute the **Singular Value Decomposition (SVD)** of a user-input matrix.  
- Prints **U**, **Σ**, and **Vᵀ** directly to the terminal.  
- Serves as a quick teaching/utility script for matrix factorization.

---

## Requirements
- Python 3.9+
- NumPy  
- Matplotlib (for Bloch sphere plots)  
- Qiskit (for Clifford operators)

Install all dependencies at once:
```bash
pip install -r requirements.txt
```
---

## Run

From the repo root, run any script directly, for example:
```bash
python "L1 Norm Approx.py"
python random_clifford_eigenvectors.py
python SVD.py
```

---

## Project Structure

- `L1 Norm Approx.py` — Rank-1 approximation with L1 error
- `random_clifford_eigenvectors.py` — Random Clifford eigenvector sampling & Bloch plots
- `SVD.py` — Simple CLI SVD
- `README.md` — Project overview
- `requirements.txt` — Python dependencies
- `.gitignore` — Ignore caches and venvs
- `LICENSE` — MIT License

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE)

