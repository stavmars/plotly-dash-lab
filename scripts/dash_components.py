# Import necessary libraries
import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html

# Load the dataset
df_restaurants = pd.read_csv("datasets/tripadvisor_restaurants_greece.csv")

# Sort the DataFrame by 'total_reviews_count' in descending order to get the top 10 restaurants
top_restaurants = df_restaurants.sort_values(
    by="total_reviews_count", ascending=False
).head(10)

# Create the bar chart with Plotly Express
fig = px.bar(
    top_restaurants,
    x="restaurant_name",
    y="total_reviews_count",
    labels={
        "restaurant_name": "Restaurant Name",
        "total_reviews_count": "Total Reviews",
    },
)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the application HTML layout
app.layout = html.Div(
    children=[
        html.H1("Top 10 Restaurants in Greece", style={"color": "blue"}),
        html.H2("based on the total number of reviews", style={"color": "darkgrey"}),
        dcc.Graph(figure=fig),
    ]
)

# Start the Dash server with debug mode enabled for development
if __name__ == "__main__":
    app.run_server(debug=True)
