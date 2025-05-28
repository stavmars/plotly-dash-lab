import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Load restaurant data and filter out entries without a city or price level
df_restaurants = pd.read_csv("datasets/tripadvisor_restaurants_greece.csv")
df_restaurants = df_restaurants[df_restaurants["city"].notna() & df_restaurants["price_level"].notna()]

# Generate a list of unique city names to populate the dropdown options, sorted alphabetically
cities = df_restaurants["city"].sort_values().unique().tolist()

# Generate a list of unique price levels to populate the second dropdown
price_levels = df_restaurants["price_level"].unique().tolist()

# Initialize the Dash app and define its HTML structure
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Top 10 Restaurants in Greece", style={"color": "blue", "textAlign": "center"}),
    html.H2("Filter by City and Price Level", style={"color": "darkgray", "textAlign": "center"}),
    html.Div([
        html.Label("Select a City:", style={"font-size": "20px", "margin-bottom": "10px", "margin-top": "20px"}),
        dcc.Dropdown(
            id="city-dropdown",
            options=cities,
            value="Athens",  # Set default value to Athens
            clearable=False,
            style={"width": "300px"}
        ),
    ]),
    html.Div([
        html.Label("Select Price Level:", style={"font-size": "20px", "margin-bottom": "10px", "margin-top": "20px"}),
        dcc.Dropdown(
            id="price-level-dropdown",
            options=price_levels,
            value=price_levels[0],  # Set default value to the first price level
            clearable=False,
            style={"width": "300px"}
        ),
    ]),
    dcc.Graph(id="bar-chart"),
])

# Callback function to update the bar chart based on selected city and price level
@app.callback(
    Output("bar-chart", "figure"), 
    [Input("city-dropdown", "value"), Input("price-level-dropdown", "value")]
)
def update_chart(selected_city, selected_price_level):
    filtered_df = df_restaurants[(df_restaurants["city"] == selected_city) & (df_restaurants["price_level"] == selected_price_level)]
    top_restaurants = filtered_df.sort_values(by="total_reviews_count", ascending=False).head(10)
    fig = px.bar(
        top_restaurants,
        x="restaurant_name",
        y="total_reviews_count",
        title=f"Top 10 {selected_price_level} Restaurants in {selected_city}",
        labels={"restaurant_name": "Restaurant Name", "total_reviews_count": "Total Reviews"}
    )
    return fig

# Execute the application server with debug enabled
if __name__ == "__main__":
    app.run(debug=True)
