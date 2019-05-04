import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import numpy as np

df = pd.read_csv('data/abalone.csv')

trace0 = go.Box(x='first',
                y=df['rings'].sample(n=20,replace=False),
                name='first')

trace1 = go.Box(x='second',
                y=df['rings'].sample(n=20,replace=False),
                name='second',
                boxpoints='all',
                jitter=0.1,
                pointpos=0)

data = [trace0,trace1]

pyo.plot(data)
