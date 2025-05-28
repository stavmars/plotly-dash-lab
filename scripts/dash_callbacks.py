import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Load restaurant data and filter out entries without a city
df_restaurants = pd.read_csv("datasets/tripadvisor_restaurants_greece.csv")
df_restaurants = df_restaurants[df_restaurants["city"].notna()]


# Generate a list of unique city names to populate the dropdown options, sorted alphabetically
cities = df_restaurants["city"].sort_values().unique().tolist()


# Initialize the Dash app and define its HTML structure
app = dash.Dash(__name__)
app.layout = html.Div(
    [
        html.H1(
            "Top 10 Restaurants in Greece",
            style={"color": "blue", "textAlign": "center"},
        ),
        html.H2("Filter by City", style={"color": "darkgray", "textAlign": "center"}),
        html.Div(
            [
                html.Label(
                    "Select a City:",
                    style={
                        "font-size": "20px",
                        "margin-bottom": "10px",
                        "margin-top": "20px",
                    },
                ),
                dcc.Dropdown(
                    id="city-dropdown",
                    options=cities,
                    value="Athens",  # Set default value to Athens
                    clearable=False,
                    style={"width": "300px"},
                ),
            ]
        ),
        dcc.Graph(id="bar-chart"),
    ]
)


# Callback function to update the bar chart when a different city is selected
@app.callback(Output("bar-chart", "figure"), Input("city-dropdown", "value"))
def update_chart(selected_city):
    filtered_df = df_restaurants[df_restaurants["city"] == selected_city]
    top_restaurants = filtered_df.sort_values(
        by="total_reviews_count", ascending=False
    ).head(10)
    fig = px.bar(
        top_restaurants,
        x="restaurant_name",
        y="total_reviews_count",
        title=f"Top 10 Restaurants in {selected_city}",
        labels={
            "restaurant_name": "Restaurant Name",
            "total_reviews_count": "Total Reviews",
        },
    )
    return fig


# Execute the application server with debug enabled
if __name__ == "__main__":
    app.run(debug=True)
