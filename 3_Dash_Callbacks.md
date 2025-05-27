# Dash Callbacks: Adding Interaction to Dashboards

In the previous section, we explored how `app.layout` shapes the visual structure of Dash applications using HTML and core components. This section introduces callbacks, powerful functions in Dash that respond to user interactions to dynamically update app content.

## Understanding and Implementing Callbacks

A **callback** in Dash is a Python function triggered automatically when the property of an input component changes. It's designed to make Dash applications interactive by updating outputs based on user inputs.

### How Callbacks Work

Callbacks in Dash applications rely on the `@app.callback` decorator—a special function that modifies or enhances another function—to define their interaction and operation:

- **Inputs**: Inputs are the properties of UI components that capture user interactions, such as a new selection in a dropdown menu, text entered into a field, or a new position on a slider. When a user modifies the value of these components, it triggers an update in the application by executing the corresponding callback function.

- **Outputs**: Outputs determine which parts of the application should be updated in response to these interactions. For instance, changing a dropdown selection might refresh a graph, update displayed text, or alter other component properties based on the new input.


To implement a callback, you:
1. **Define the function** to specify how the data should transform when inputs change.
2. **Decorate the function** with `@app.callback`, linking inputs and outputs.
3. **Connect the logic** to the UI components, ensuring that user interactions lead to visible changes in the app.




## Hands-On Task 2: Dash Callbacks

In this task, you'll learn how callbacks enable interactivity within a Dash application. We will expand the example from Task 1 to allow the user to refine their analysis and find the top 10 restaurants in the city they select. For this, we'll add an interactive element—a dropdown menu for the user to select a city.

### Objective:
Develop a dashboard with the following components:

- **Title**: "Top 10 Restaurants in Greece"
    - **Color**: Blue
    - **Alignment**: Center
- **Subtitle**: "Filter by City"
    - **Color**: Dark gray
    - **Alignment**: Center
- **Interactive Component**: A dropdown element to select the city, with the cities sorted alphabetically.
- **Visualization**:
    - **Bar Chart**: Displays the top 10 restaurants by total review count in the selected city.
        - **X-axis**: Restaurant Name
        - **Y-axis**: Number of Reviews
        - **Chart Title**: "Top 10 Restaurants in [selected city]"
            - This title should update based on the city selected.

## Steps to Build the Dashboard for Task 2

1. **Create a New File**
   - Create a new Python script named `dash_callbacks.py`. This file will contain all the code for your dashboard.

2. **Import Libraries**
   - Import necessary libraries including Dash, Plotly, and Pandas to handle data manipulation and visualization:
     ```python
     import pandas as pd
     import plotly.express as px
     import dash
     from dash import dcc, html
     from dash.dependencies import Input, Output
     ```

3. **Load and Prepare the Data**
   - Load the dataset containing information about restaurants and keep only records with non-null `city`:
     ```python
     # Load restaurant data and filter out entries without a city
     df_restaurants = pd.read_csv('datasets/tripadvisor_restaurants_greece.csv')
     df_restaurants = df_restaurants[df_restaurants['city'].notna()]
     ```

4. **Prepare Dropdown Options**
   - Create a sorted list of unique cities from the dataset to populate the dropdown menu:
     ```python
     # Generate a list of unique city names to populate the dropdown options, sorted alphabetically
     cities = df_restaurants["city"].sort_values().unique().tolist()
     ```

5. **Application Layout**
   - Set up the Dash application and define the HTML layout, including the title, subtitle, dropdown menu, and bar chart area:
     ```python
     # Initialize the Dash app and define its HTML structure
     app = dash.Dash(__name__)
     app.layout = html.Div([
         html.H1("Top 10 Restaurants in Greece", style={"color": "blue", "textAlign": "center"}),
         html.H2("Filter by City", style={"color": "darkgray", "textAlign": "center"}),
         html.Div([
             html.Label('Select a City:', style={'font-size': '20px', 'margin-bottom': '10px', 'margin-top': '20px'}),
             dcc.Dropdown(
                 id='city-dropdown',
                 options=cities,
                 value='Athens',  # Set default value to Athens
                 clearable=False,
                 style={'width': '300px'}
             )
         ]),
         dcc.Graph(id='bar-chart')
     ])
     ```

6. **Define the Callback**
   - Implement a callback function to dynamically update the bar chart based on the city selected from the dropdown:
     ```python
     # Callback function to update the bar chart when a different city is selected
     @app.callback(
         Output('bar-chart', 'figure'),
         Input('city-dropdown', 'value')
     )
     def update_chart(selected_city):
         filtered_df = df_restaurants[df_restaurants['city'] == selected_city]
         top_restaurants = filtered_df.sort_values(by="total_reviews_count", ascending=False).head(10)
         fig = px.bar(
             top_restaurants,
             x="restaurant_name",
             y="total_reviews_count",
             title=f"Top 10 Restaurants in {selected_city}",
             labels={"restaurant_name": "Restaurant Name", "total_reviews_count": "Total Reviews"}
         )
         return fig
     ```

7. **Start the App**
   - Launch the application to enable interactive exploration on a local web server:
     ```python
     # Execute the application server with debug enabled
     if __name__ == '__main__':
         app.run(debug=True)
     ```


### Practice Exercise

After completing the initial dashboard setup, expand it by integrating an additional interactive element:

1. **Change the subtitle of the dashboard**:
      - **New Subtitle**: "Filter by City and Price Level"

2. **Add a New Dropdown**:
   - Include a second dropdown to allow users to select a value for the `price_level` column. Add a label "Select Price Level:" above this dropdown. Populate the dropdown using the distinct values from this column.
      - This can be done by extracting unique values from the `price_level` column in your dataset similar to how cities were extracted.

3. **Modify the Callback**:
   - Update the callback decorator to accept two inputs: the value from the selected city dropdown and the value from the price level dropdown.
   - Adjust the callback function to dynamically update the chart based on both the selected city from the first dropdown and the price level from the new dropdown.
   - Update the chart title to dynamically include the name of the selected price level, formatted as:
     ```plaintext
     Top 10 [selected_price_level] Restaurants in [selected city]
     ```
    - Ensure that the title updates correctly when either dropdown selection changes, reflecting both the city and the price level in the visualization.


<!-- For a complete solution to these exercises, visit [this link](https://github.com/stavmars/plotly-dash-lab/blob/main/scripts/dash_callbacks_practice.py). -->


<br>

**[← Previous](2_Dash_Components.md) | [Next →](4_Advanced_Dash_Example.md)**
---


