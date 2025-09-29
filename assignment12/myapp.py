# myapp.py
import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import plotly.data as pldata
import pandas as pd

# Load dataset
df = pldata.gapminder()
countries = df['country'].unique()

app = dash.Dash(__name__)
server = app.server

# Create app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("GDP Growth by Country"),
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': c, 'value': c} for c in countries],
        value='Canada',
        clearable=False
    ),
    dcc.Graph(id='gdp-growth')
])

@app.callback(
    Output('gdp-growth', 'figure'),
    Input('country-dropdown', 'value')
)
def update_graph(selected_country):
    filtered_df = df[df['country'] == selected_country]
    fig = px.line(filtered_df, x='year', y='gdpPercap',
                  title=f"GDP per Capita Growth for {selected_country}")
    return fig

if __name__ == '__main__':
    app.run(debug=True)
