import plotly
import pandas as pd
# Load dats
df = pd.read_cvs("公車_運量統.cvs")
df.columns = [col.replace("AAPL.","")for col in df.columns]
print(df)

import plotly.graph_objects as go
line1 = go.Scatter(x=df['Date'], y=df['Close'], name='Close')
fig = go.Figure(line1)
fig.show()