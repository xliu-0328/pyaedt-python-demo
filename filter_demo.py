import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


# --------------------------------------------------
# Simple Low-Pass Filter Demo
# --------------------------------------------------

# Filter specifications
cutoff_frequency = 1e6      # 1 MHz
filter_order = 4

# Create a 4th-order Butterworth low-pass filter
b, a = signal.butter(
    filter_order,
    2 * np.pi * cutoff_frequency,
    btype="low",
    analog=True
)

# Frequency sweep: 10 kHz to 100 MHz
frequency = np.logspace(4, 8, 1000)

# Calculate frequency response
w = 2 * np.pi * frequency
w, h = signal.freqs(b, a, worN=w)

# Convert magnitude to dB
magnitude_db = 20 * np.log10(np.abs(h))

# Find response near cutoff frequency
cutoff_index = np.argmin(np.abs(frequency - cutoff_frequency))

print("Filter Demo")
print("----------------------")
print(f"Order: {filter_order}")
print(f"Cutoff frequency: {cutoff_frequency / 1e6:.1f} MHz")
print(f"Gain at cutoff: {magnitude_db[cutoff_index]:.2f} dB")

# Plot frequency response
plt.figure(figsize=(8, 5))

plt.semilogx(
    frequency / 1e6,
    magnitude_db
)

plt.axvline(
    cutoff_frequency / 1e6,
    linestyle="--",
    label="Cutoff frequency"
)

plt.xlabel("Frequency (MHz)")
plt.ylabel("Magnitude (dB)")
plt.title("4th-Order Butterworth Low-Pass Filter")
plt.grid(True, which="both")
plt.legend()

plt.show()