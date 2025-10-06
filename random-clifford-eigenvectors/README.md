# Random Clifford Eigenvectors (CLI Tool)

Generates random **1-qubit Clifford operators**, extracts an eigenvector from each, converts it to **Bloch sphere** coordinates (angles + Cartesian), and plots the results. Useful for visualizing eigenstate distributions under the Clifford group.

---

## Requirements
- Python 3.9+
- NumPy
- Matplotlib
- Qiskit

Install (from the repo root or this folder):
```bash
pip install -r ../requirements.txt
# or individually:
# pip install numpy matplotlib qiskit
```

---

## Run

From this folder:
```bash
python random_clifford_eigenvectors.py
```
The script will:
- Sample random 1-qubit Clifford operators
- Compute an eigenvector for each
- Convert to Bloch angles and (x, y, z) coordinates
- Show a scatter plot and/or Bloch sphere visualization

---

## Notes

- If plots don’t appear, ensure a GUI backend is available (e.g., install your OS’s matplotlib backend or use matplotlib.use('Agg') to save figures).
- You can adjust the number of samples and random seed inside the script.
- Qiskit installation can be larger; consider a virtual environment.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE)
