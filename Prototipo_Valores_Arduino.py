import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
f = 3600  # Frequency of triangular wave
t = np.arange(0, 0.00833, 1 / (f * 100))  # Time vector
sinwave = np.sin(377 * t) * 1  # Sine and -Sine wave at 60Hz
minsin = -sinwave

triangular_wave = 1 * signal.sawtooth(2 * np.pi * f * t, width=0.5)  # Creating a triangular wave
Vq1 = (sinwave > triangular_wave) * 5  # Obtaining Q1 pulses
Vq4 = (minsin < triangular_wave) * 5  # Obtaining Q4 pulses
Vq2 = (minsin > triangular_wave) * 5  # Obtaining Q2 pulses
Vq3 = (sinwave < triangular_wave) * 5  # Obtaining Q3 pulses
plt.figure(1)
plt.subplot(4,1,1)
plt.plot(t, Vq1)
plt.subplot(4,1,2)
plt.plot(t, Vq4)
plt.subplot(4,1,3)
plt.plot(t, Vq2)
plt.subplot(4,1,4)
plt.plot(t, Vq3)
plt.show()
# Assuming you have a numpy array with time and value
# Example array
data = np.array(list(zip(t, Vq1)))


time_intervals = []

previous_value = data[0, 1]
start_time = data[0, 0]

for i in range(1, len(data)):
    current_time, current_value = data[i]

    if current_value != previous_value:
        time_intervals.append((current_time - start_time) * 1e6)  # Convert to microseconds
        start_time = current_time

    previous_value = current_value

# If the last value is 1, we need to consider the remaining time as well
if previous_value == 1:
    time_intervals.append((data[-1, 0] - start_time) * 1e6)  # Convert to microseconds

print('Time Vq1:',time_intervals)
print("Length of Time Intervals:", len(time_intervals))
