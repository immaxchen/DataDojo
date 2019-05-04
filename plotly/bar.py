import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('data/mocksurvey.csv',index_col=0)

data = [go.Bar(y=df.index,x=df[col],name=col,orientation='h') for col in df.columns]

layout = go.Layout(title='Survey Results',barmode='stack')

figure = go.Figure(data=data,layout=layout)
pyo.plot(figure)
