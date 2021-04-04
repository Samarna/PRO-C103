import pandas as pd 
import plotly_express as px 

df = pd.read_csv("graphData.csv")

fig2 = px.scatter(df, x="date",y="cases",color="country",size_max=60)
fig2.show()