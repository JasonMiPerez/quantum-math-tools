import random, math, cmath
import numpy as np
import matplotlib.pyplot as plt
from qiskit.quantum_info import random_clifford
from mpl_toolkits.mplot3d import Axes3D  

# Returns floating point value for an angle theta, arccot(theta)
def acot(angle: float) -> float:
    return math.atan2(1.0, angle)

# Generates a 1-qubit clifford matrix in the form of a numpy matrix.
def generate_random_clifford():
    clifford_operator = random_clifford(1) # Clifford matrix in qiskit.
    return clifford_operator.to_operator().data  # Changes qiskit Clifford matrix to numpy Clifford matrix and returns it.

# Returns a random eigenvector from a numpy Clifford matrix in the form of a numpy array.
def random_eigenvector_of_clifford(clifford: np.ndarray) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eig(clifford)  # Retrive eigenvectors (and eigenvalues) from numpy Clifford matrix and returns it as a numpy matrix (columns are eigenvectors)
    random_index = random.choice([0, 1]) # Generates 0 or 1 randomly.
    eigenvector = eigenvectors[:, random_index] # Retrives the eigenvector at index "random_index".
    eigenvector = eigenvector / np.linalg.norm(eigenvector) # Normalizes the eigenvector (numpy eigenvectors are not necessarily normalized).
    return eigenvector # Returns the eigenvector.

# For any value n where n is a positive integer, samples n eigenvectors and returns in the form of an numpy matrix.
def sample_random_clifford_eigenvectors(number_of_eigenvectors: int) -> np.ndarray:
    eigenvectors = np.zeros((number_of_eigenvectors, 2), dtype=complex) # Intilizes "number_of_eigenvectors" size numpy matrix of dimensions 2 x "number_of_eigenvectors". 
    for index in range(number_of_eigenvectors): # Loops through indeces 0 through "number_of_eigenvectors" - 1.
        clifford_operator = generate_random_clifford() # Generate random numpy clifford operator.
        eigenvectors[index] = random_eigenvector_of_clifford(clifford_operator) # Retrive random eigenvector from that numpy clifford operator and stores it in eigenvectors are index "index".
    return eigenvectors # Returns eigenvectors as numpy matrix.


# Returns angles for projecting the eigenvectors of Clifford matrices.
def bloch_angles_for_state(state):
    alpha, beta = state # Retrive amplitudes of state.
    norm = np.linalg.norm(state) # Retrive norm of state.
    # Checks if norm is 0 just in case (numpy eigenvectors will not automatically have norm 1).
    if norm == 0:
        raise ValueError("Zero vector is not a valid state.")
    alpha, beta = alpha/norm, beta/norm # Normalizes amplitudes.
    # Checks if beta == 0, and if it is, returns angles 0 and 1 respectivly.
    if abs(beta) < 1e-12:
        return 0.0, 1.0
    w = alpha / beta # Divide amplitudes.
    f = abs(w) # Return absolute value of w.
    theta = cmath.phase(w) # Return phase of w.
    phi = 2 * acot(f) # cot(f) and multiply by 2.
    return float(theta), math.cos(phi)  # returns returns theta and cos(phi).

# ---------- Delete this if you don't want to plot on bloch sphere ----------

# Retrived Cartesian coordinates of eigenvectors for bloch sphere.
def bloch_cartesian_from_state(state): 
    alpha, beta = state # Retrive amplitudes of state.
    norm = np.linalg.norm(state) # Retrive norm of state.
    # Checks if norm is 0 just in case (numpy eigenvectors will not automatically have norm 1).
    if norm == 0:
        raise ValueError("Zero vector is not a valid state.")
    alpha, beta = alpha/norm, beta/norm # Normalizes amplitudes.
    # Computes bloch sphere coordinates
    x = 2 * np.real(np.conj(alpha) * beta)
    y = 2 * np.imag(np.conj(alpha) * beta)
    z = np.abs(alpha)**2 - np.abs(beta)**2
    return float(x), float(y), float(z) # Returns bloch sphere coordinates as floating points.

# ---------- Delete this if you don't want to plot on bloch sphere ----------

# Asks user to input number of eigenvectors that they want to sample and retrives their angles for projection (stores theta's and cos(phi)'s in a list). 
number_of_eigenvectors = int(input("Enter number of eigenvectors you want to sample from: "))
eigenvectors = sample_random_clifford_eigenvectors(number_of_eigenvectors)
angle_pairs = [bloch_angles_for_state(eigenvector) for eigenvector in eigenvectors]
thetas = [pair[0] for pair in angle_pairs]
cosphis = [pair[1] for pair in angle_pairs]

plt.figure(figsize=(5,4))
plt.scatter(thetas, cosphis, s=14)
plt.xlabel("theta")
plt.ylabel("cos(phi)")
plt.title("2D projection from alpha and beta (Clifford eigenvectors)")
plt.tight_layout()
plt.show()

# ---------- Delete this if you don't want to plot on bloch sphere ----------

# Retrives cartesian coordinates from eigenvectors and plots them on the bloch sphere.
xs, ys, zs = [], [], []
for eigenvector in eigenvectors:
    x, y, z = bloch_cartesian_from_state(eigenvector)
    xs.append(x); ys.append(y); zs.append(z)

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection="3d")

u = np.linspace(0, 2*np.pi, 60)
t = np.linspace(0, np.pi, 30)
sx = np.outer(np.cos(u), np.sin(t))
sy = np.outer(np.sin(u), np.sin(t))
sz = np.outer(np.ones_like(u), np.cos(t))
ax.plot_wireframe(sx, sy, sz, alpha=0.2, linewidth=0.5)

ax.scatter(xs, ys, zs, s=20)
ax.set_xlabel("X"); ax.set_ylabel("Y"); ax.set_zlabel("Z")
ax.set_title("Random eigenvectors of 1-qubit Cliffords on the Bloch sphere")
ax.set_box_aspect([1, 1, 1])
plt.show()

# ---------- Delete this if you don't want to plot on bloch sphere ----------
