import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

random_x = np.random.randn(1000)
random_y = np.random.randn(1000)

trace = go.Scatter(
    x=random_x,
    y=random_y,
    mode='markers'
)

data = [trace]

layout = go.Layout(
    title='Gaussian',
    xaxis=dict(title='X'),
    yaxis=dict(title='Y',scaleanchor='x'),
    hovermode ='closest'
)

figure = go.Figure(data=data,layout=layout)

pyo.plot(figure)
