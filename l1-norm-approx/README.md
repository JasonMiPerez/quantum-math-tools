# L1 Norm Rank-1 Approximation (CLI Tool)

A small Python command-line program that approximates a **2×2 complex matrix** with a **rank-1** matrix by minimizing the **L1 error** (sum of entrywise absolute differences).  
It samples candidate matrices under the rank-1 constraint (`a*d = b*c`) and keeps the best one found.

---

## Requirements
- Python 3.9+
- NumPy

---

## Run
From this folder:
```bash
python "L1 Norm Approx.py"
```
You will be prompted to enter the four complex entries of the matrix (e.g., 1+2j).
The script repeatedly samples rank-1 candidates and tracks the **smallest L1 error**.
Type stop at the prompt to end the search and print the best result found.

--- 

## Notes 

- Rank-1 constraint is enforced by setting the fourth entry as `(b*c)/a` (when `a ≠ 0`).
- Because the search is randomized, results can vary across runs.
- You can adjust sampling bounds and stopping behavior inside the script to trade off speed vs. quality.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE)
