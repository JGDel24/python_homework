import plotly.express as px
import plotly.data as pldata
import pandas as pd
import webbrowser
import os

df = pldata.wind(return_type='pandas')

print("First 10 rows:")
print(df.head(10))
print("\nLast 10 rows:")
print(df.tail(10))


df['strength'] = pd.to_numeric(df['strength'].astype(str).str.replace(r"[^\d.]", "", regex=True), errors='coerce')

df = df.dropna(subset=['strength', 'frequency', 'direction'])

print("\nAfter cleaning:")
print(df.head())

fig = px.scatter(
    df,
    x='strength',
    y='frequency',
    color='direction',
    title='Wind Strength vs Frequency',
    labels={'strength':'Wind Strength', 'frequency':'Frequency'},
    hover_data=['direction']
)

html_file = "wind.html"
fig.write_html(html_file)
webbrowser.open('file://' + os.path.realpath(html_file))