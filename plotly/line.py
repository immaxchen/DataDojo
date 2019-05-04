import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

from datetime import datetime
def parseTime(s):
    return datetime.strptime(s,'%H:%M').time()

df = pd.read_csv('data/2010YumaAZ.csv', converters={'LST_TIME': parseTime})
df = df.pivot(columns='DAY', index='LST_TIME', values='T_HR_AVG')

data = [go.Scatter(x=df.index,
                   y=df[day],
                   mode='markers+lines',
                   name=day) for day in df.columns]

layout = go.Layout(title='2010 Yuma AZ Temperature',
                   xaxis=dict(title='hours'),
                   yaxis=dict(title='degree celsius'))

figure = go.Figure(data=data,layout=layout)
pyo.plot(figure)
