import cmath

z = complex(input())

# Calculate the magnitude (r) and phase angle (phi) using cmath functions
r = abs(z)
phi = cmath.phase(z)

# Print the magnitude and phase angle in polar coordinates
print(r)
print(phi)
