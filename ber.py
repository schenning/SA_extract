import numpy as np
from scipy.special import erfc
import matplotlib.pyplot as plt
import math
import random


def gen_random_binary_digit():
    # 0 or 1 drawn from an uniform probability distribution
    return random.choices([0,1], [0.5,0.5])[0]


N = 10**6  # number of bits or symbols
np.random.seed(100)  # initializing the random seed
np.random.seed(200)  # initializing the random seed for Gaussian noise

# Transmitter
ip = np.random.rand(N) > 0.5  # generating 0, 1 with equal probability
s = 2 * ip - 1  # BPSK modulation: 0 -> -1, 1 -> 1
n = (1 / np.sqrt(2)) * (np.random.randn(N) + 1j * np.random.randn(N))  
Eb_N0_dB = np.arange(-3, 20)  # multiple Eb/N0 values

nErr = np.zeros(len(Eb_N0_dB)) 

for ii in range(len(Eb_N0_dB)):
    # Noise addition
    y = s + 10 ** (-Eb_N0_dB[ii] / 20) * n  # additive white Gaussian noise

   
    ipHat = np.real(y) > 0


    # Counting the errors
    nErr[ii] = np.sum(ip != ipHat)


simBer = nErr / N  
theoryBer = 0.5 * erfc(np.sqrt(10 ** (Eb_N0_dB / 10))) 
plt.figure()
plt.semilogy(Eb_N0_dB, theoryBer, 'b.-', label='theory')

plt.semilogy(Eb_N0_dB, simBer, 'mx-', label='simulation')
plt.axis([-3, 20, 10 ** -9, 0.5])
plt.grid(True)
plt.legend()
plt.xlabel('Eb/No, dB')
plt.ylabel('Bit Error Rate')
plt.title('Bit error probability curve for BPSK modulation')
plt.show()

print(simBer)