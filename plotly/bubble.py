import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('data/mpg.csv')
df['horsepower'] = pd.to_numeric(df['horsepower'],errors='coerce')

trace = go.Scatter(x=df['displacement'],
                   y=df['acceleration'],
                   text=df['name'],
                   mode='markers',
                   marker=dict(size=df['horsepower']/10,
                               color=df['cylinders'],
                               showscale=True))

data = [trace]

layout = go.Layout(title='acceleration vs displacement',
                   xaxis=dict(title='displacement'),
                   yaxis=dict(title='acceleration'))

figure = go.Figure(data=data,layout=layout)
pyo.plot(figure)
