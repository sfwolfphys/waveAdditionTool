import matplotlib.pyplot as plt
import numpy as np
from shiny.express import input, render, ui
from shinywidgets import render_plotly
from waveAddition import *


ui.page_opts(title="Wave Addition Tool",
    window_title="Wave Addition")


with ui.sidebar():
  ui.input_slider("nSources", "Number of sources", min=1, max=20, value=2)
  ui.input_slider("deltaAdj", "Path difference between adjacent sources", 
    min=0, max=1, value=0.1, step=0.05)


@render.plot(alt='Wave Plot')
def thePlot():
  theFig = waveAdditionPlot(input.nSources(),input.deltaAdj())
  return theFig
