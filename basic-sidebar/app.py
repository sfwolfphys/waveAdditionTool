from shiny.express import input, render, ui
from waveAddition import *

ui.page_opts(title="Wave Addition Tool",
    window_title="Wave Addition")


with ui.sidebar():
  ui.input_slider("nSources", "Number of sources", min=1, max=20, value=2)
  ui.input_slider("deltaAdj", r"Path difference between adjacent sources (in terms of wavelength)", 
    min=0, max=1, value=0.1, step=0.001)

@render.plot(alt='Wave Plot')
def thePlot():
  theFig = waveAdditionPlot(input.nSources(),input.deltaAdj())
  return theFig
