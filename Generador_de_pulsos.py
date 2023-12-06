import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal

f = 3600  # Frecuencia señal triangular
t = np.arange(0, 0.0166667, 1 / (f * 50))  # Vector de tiempos
sinwave = np.sin(377 * t)*1  # Seno y -Seno a 60Hz
minsin = -sinwave

triangular_wave = 1 * signal.sawtooth(2 * np.pi * f * t, width=0.5)  # Creación de señal triangular
Vq1 = (sinwave > triangular_wave) * 32  # Obtención de pulsos Q1
Vq4 = (minsin < triangular_wave) * 20  # Obtención de pulsos Q4

Vq2 = (minsin > triangular_wave) * 32  # Obtención de pulsos Q2
Vq3 = (sinwave < triangular_wave) * 20  # Obtención de pulsos Q3
plt.figure(1)
plt.subplot(4,1,1)
plt.plot(t, Vq1)
plt.subplot(4,1,2)
plt.plot(t, Vq4)
plt.subplot(4,1,3)
plt.plot(t, Vq2)
plt.subplot(4,1,4)
plt.plot(t, Vq3)


pq1 = Vq1.astype(int)
pq4 = Vq4.astype(int)
pq2 = Vq2.astype(int)
pq3 = Vq3.astype(int)

data = {'t': t, 'Vq1': pq1}
df = pd.DataFrame(data)
df.to_csv('32VPQ1.tsv', sep='\t', index=False, header=False)  # Elimina el encabezado y utiliza '\t' como separador

data = {'t': t, 'Vq4': pq4}
df = pd.DataFrame(data)
df.to_csv('20VPQ4.tsv', sep='\t', index=False, header=False)

data = {'t': t, 'Vq2': pq2}
df = pd.DataFrame(data)
df.to_csv('32VPQ2.tsv', sep='\t', index=False, header=False)

data = {'t': t, 'Vq3': pq3}
df = pd.DataFrame(data)
df.to_csv('20VPQ3.tsv', sep='\t', index=False, header=False)

plt.show()
