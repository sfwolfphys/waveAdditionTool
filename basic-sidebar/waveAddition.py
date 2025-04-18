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
  fig, ax = plt.subplots()
  ax.plot(x,totWave,label='Total Wave',lw=5)
  ax.set_ylim(-N-0.5,N+0.5)
  ax.set_xlabel(r'$x (\lambda)$')
  ax.set_ylabel('Wave output (Single Amplitude)')
  for i in range(N):
    y = wave(x,i*delta)
    ax.plot(x,y,label=f'Wave {i+1}')
  ax.legend(bbox_to_anchor=(1.25,1))
  fig.suptitle(f'Path difference = {delta:.2f}')
  return fig
