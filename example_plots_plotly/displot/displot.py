import plotly.offline as pyo
import plotly.figure_factory as ff
import scipy
import numpy as np

x1 = np.random.rand(500)
x2 = np.random.rand(500)+2

hisdata = [x1,x2]

group_labels = ['Distribucion x1','Distribucion x2']

fig = ff.create_distplot(hisdata,group_labels,bin_size=[2,1])

pyo.plot(fig, filename='displot.html')