import numpy as np
import random

# Input the matrix M
M = np.array([complex(input(f"Enter M[{i}] (e.g., real+imagj): ")) for i in range(4)])
best_Mh = np.zeros(4, dtype=complex)
min_L1 = float('inf')

while True:
    try:
        R = 2
        Mh = np.zeros(4, dtype=complex)

        # Generate Mh[0]
        lowerb_real = M[0].real - R
        upperb_real = M[0].real + R
        lowerb_imag = M[0].imag - R
        upperb_imag = M[0].imag + R
        Mh[0] = complex(random.uniform(lowerb_real, upperb_real), random.uniform(lowerb_imag, upperb_imag))
        R -= abs(M[0] - Mh[0])

        if R < 1:
            continue

        # Generate Mh[1]
        lowerb_real = M[1].real - R
        upperb_real = M[1].real + R
        lowerb_imag = M[1].imag - R
        upperb_imag = M[1].imag + R
        Mh[1] = complex(random.uniform(lowerb_real, upperb_real), random.uniform(lowerb_imag, upperb_imag))
        R -= abs(M[1] - Mh[1])

        if R < 1:
            continue

        # Generate Mh[2]
        lowerb_real = max(M[2].real - R, M[2].real - (R - 1))
        upperb_real = min(M[2].real + R, M[2].real + (R - 1))
        lowerb_imag = max(M[2].imag - R, M[2].imag - (R - 1))
        upperb_imag = min(M[2].imag + R, M[2].imag + (R - 1))
        if lowerb_real > upperb_real or lowerb_imag > upperb_imag:
            continue

        Mh[2] = complex(random.uniform(lowerb_real, upperb_real), random.uniform(lowerb_imag, upperb_imag))

        if Mh[0] == 0:
            continue

        # Calculate Mh[3]
        Mh[3] = (Mh[1] * Mh[2]) / Mh[0]

        # Calculate L1 norm
        L1 = sum(abs(M[i] - Mh[i]) for i in range(4))

        if 1 <= L1 <= 2 and L1 < min_L1:
            min_L1 = L1
            best_Mh = Mh.copy()

        # Prompt user to stop or continue
        command = input("Type 'stop' to end or press Enter to continue: ").strip()
        if command.lower() == 'stop':
            break
    except Exception as e:
        print("An error occurred. Restarting iteration.")

print(f"Smallest L1 norm: {min_L1}")
print(f"Corresponding Mh values: {best_Mh}")
