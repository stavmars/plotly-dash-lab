# Create a file named hello_dash.py and paste the following code:
import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Hello Dash!"),
    html.Div("Your first Dash app.")
])

if __name__ == '__main__':
    app.run(debug=True)