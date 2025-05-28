import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Load the dataset
df_restaurants = pd.read_csv("datasets/tripadvisor_restaurants_greece.csv")

# Ensure there are no null values in the 'region' column
df_restaurants = df_restaurants[df_restaurants["region"].notna()]

# Step 1: Create a list of unique regions from the dataset

# ----- > Your code here
regions = df_restaurants["region"].unique().tolist()


# Initialize the Dash app
app = dash.Dash(__name__)


# Define the application layout
app.layout = html.Div(
    [
        html.H1(
            "Restaurants in Greece Dashboard",
            style={"color": "blue", "textAlign": "center"},
        ),
        html.Div(
            [
                html.Label(
                    "Select Regions:",
                    style={
                        "display": "inline-block",
                        "font-size": "20px",
                        "margin-bottom": "10px",
                    },
                ),
                # Step 2: Create a Region Selection Dropdown
                # - Fill in code here to create a dropdown with id `region-dropdown` that allows multiple selections of regions
                # - Use the 'regions' list to populate the dropdown options.
                dcc.Dropdown(
                    id="region-dropdown",
                    options=regions,
                    value=None,
                    multi=True,
                    placeholder="Select one or more regions",
                    clearable=True,
                    style={"width": "500px"},
                ),
            ],
            style={"margin-bottom": "20px"},
        ),
        html.Div(
            [
                html.Label(
                    "Select Rating Range:",
                    style={
                        "display": "inline-block",
                        "font-size": "20px",
                        "margin-bottom": "20px",
                    },
                ),
                # Step 3: Create an average rating Range Slider
                # - Use the dcc.RangeSlider component to create a range slider with id `rating-range-slider` for filtering by average rating.
                # - Set the minimum to 0, the maximum to 5, and step to 0.1.
                dcc.RangeSlider(
                    id="rating-range-slider",
                    min=0,
                    max=5,
                    value=[
                        0,
                        5,
                    ],
                    marks={i: str(i) for i in range(0, 6)},
                    step=0.1,
                ),
            ],
            style={"width": "500px", "margin-top": "20px", "margin-bottom": "20px"},
        ),
        # First row: Top Restaurants bar chart and pie chart for price level
        html.Div(
            [
                html.Div(
                    [dcc.Graph(id="top-restaurants-bar-chart")],
                    style={"display": "inline-block", "width": "50%"},
                ),
                html.Div(
                    [dcc.Graph(id="price-level-pie-chart")],
                    style={"display": "inline-block", "width": "50%"},
                ),
            ],
            style={"margin-bottom": "50px"},
        ),
        # Second row: Bar Chart for Cuisine Popularity
        html.Div([dcc.Graph(id="top-cuisines-bar-chart")]),
    ],
    style={"padding": "20px"},
)


@app.callback(
    [
        Output(component_id="top-restaurants-bar-chart", component_property="figure"),
        Output(component_id="price-level-pie-chart", component_property="figure"),
        Output(component_id="top-cuisines-bar-chart", component_property="figure"),
    ],
    [
        Input(component_id="region-dropdown", component_property="value"),
        Input(component_id="rating-range-slider", component_property="value"),
    ],
)
def update_charts(selected_regions, rating_range):
    top_restaurants_fig = None
    price_level_fig = None
    top_cuisines_fig = None

    if selected_regions:
        filtered_df = df_restaurants[df_restaurants["region"].isin(selected_regions)]
    else:
        filtered_df = df_restaurants
    filtered_df = filtered_df[
        (filtered_df["avg_rating"] >= rating_range[0])
        & (filtered_df["avg_rating"] <= rating_range[1])
    ]
    # Step 4: Sort the filtered restaurants by 'total_reviews_count' in descending order to get the top 10 restaurants

    # ----- > Your code here to find the top restaurants
    top_restaurants = filtered_df.sort_values(
        by="total_reviews_count", ascending=False
    ).head(10)

    # ----- > Your code here to generate the top restaurants bar chart
    top_restaurants_fig = px.bar(
        top_restaurants,
        x="restaurant_name",
        y="total_reviews_count",
        labels={
            "restaurant_name": "Restaurant Name",
            "total_reviews_count": "Total Reviews",
        },
        title="Top 10 Restaurants by Number of Reviews",
    )
    # Step 5: Generate pie chart for price levels

    # ----- > Your code here to find the number of restaurants per price level
    price_counts = filtered_df["price_level"].value_counts()

    # ----- > Your code here to generate the pie chart to analyze restaurants per price level
    price_level_fig = px.pie(
        values=price_counts.values,
        names=price_counts.index,
        labels={"names": "Price Level", "values": "Number of Restaurants"},
        title="Distribution of Restaurants by Price Level",
    )

    # Step 6: The cuisines column is a comma-separated string. To find specific cuisines, split and explode 'cuisines' column, then aggregate by count

    # ----- > Your code here to find the number of restaurants per cuisine
    exploded_cuisines = filtered_df["cuisines"].dropna().str.split(", ").explode()
    cuisines_counts = exploded_cuisines.value_counts().head(20)

    # ----- > Your code here to generate the top cuisines bar chart
    top_cuisines_fig = px.bar(
        x=cuisines_counts.index,
        y=cuisines_counts.values,
        labels={"x": "Cuisine", "y": "Number of Restaurants"},
        title="Top 20 Cuisines Based on Number of Restaurants",
    )

    return [top_restaurants_fig, price_level_fig, top_cuisines_fig]


# Start the Dash server with debug mode enabled for development
if __name__ == "__main__":
    app.run(debug=True)
