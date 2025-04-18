from shiny.express import input, render, ui
import numpy as np
import matplotlib.pyplot as plt
from waveAddition import *

with ui.sidebar():
    ui.input_selectize("nSources", "Number of sources",choices=np.arange(2,21,1))
    ui.input_slider("deltaAdj", "Path diff", min=0, max=4, value=0.1)

@render.plot
def thePlot():
    waveAdditionPlot(input.nSources(),input.deltaAdj())