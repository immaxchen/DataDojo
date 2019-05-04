import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('data/abalone.csv')

trace = go.Histogram(x=df['length'],xbins=dict(start=0,end=1,size=0.02))

data = [trace]

layout = go.Layout(title='Shell Length')

figure = go.Figure(data=data,layout=layout)
pyo.plot(data)
