import pandas as pd
import plotly.express as px

yr_filtered = pd.read_csv('/home/hamsini.sankaran/w209/static/yr_filtered.csv')
year_data = yr_filtered[yr_filtered['year'] == 2015]
print(year_data)
fig = px.sunburst(year_data, path=['region', 'state'],  title='Regions and States')
fig.update_traces(textfont=dict(size=25), insidetextfont=dict(size=16))
fig.update_layout(margin=dict(t=40, l=0, r=0, b=0), height=600, width=1300)
fig.show()
