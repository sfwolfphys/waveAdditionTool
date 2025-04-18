import matplotlib.pyplot as plt
import numpy as np

def wave(x,delta):
    return np.sin(2*np.pi*(x+delta))

def totalWave(x,delta,N):
    tW = 0
    for i in range(N):
        tW = tW + wave(x,i*delta)
    return(tW)


def waveAdditionPlot(N,delta):
    x = np.linspace(0,3,1000)
    totWave = totalWave(x,delta,N)
    plt.plot(x,totWave,label='Total Wave')
    plt.ylim(-N-0.5,N+0.5)
    plt.xlabel(r'$x (\lambda)$')
    plt.ylabel('Wave output (Single Amplitude)')
    for i in range(N):
        y = wave(x,i*delta)
        plt.plot(x,y,label=f'Wave {i+1}')
    plt.legend()
    plt.show()