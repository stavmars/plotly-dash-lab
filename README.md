# Building Interactive Dashboards with Plotly and Dash

This lab introduces **Plotly** and **Dash** for creating interactive, web-based analytics applications with Python.

The goal of the lab is to show how we can move from static data analysis to interactive dashboards. Plotly will be used to create interactive charts, while Dash will be used to organize those charts into a web-based dashboard with interactive components such as dropdowns, sliders, and callbacks.

## The Role of Dashboards in Data Analytics

Dashboards are an important part of modern data analytics. They are used to bring together the most important information about a dataset, process, system, or business problem in a compact and interactive form.

A good dashboard does not simply show many charts on the same page. Its purpose is to help users understand what is happening, identify patterns, compare alternatives, and make decisions more quickly.

For example, a dashboard may help answer questions such as:

- Which products have the highest sales?
- Which regions perform better or worse?
- How does a metric change over time?
- Are there unusual values or outliers?
- What happens if we focus only on a specific category, city, time period, or group of users?

Dashboards are commonly used in many domains, including:

- business analytics, for monitoring sales, revenue, and customers;
- public administration, for tracking indicators and services;
- health analytics, for monitoring patients, resources, or outcomes;
- tourism analytics, for understanding visitor flows and demand;
- machine learning and data science, for monitoring experiments, model performance, and data quality.

In this lab, we will use restaurant and tourism datasets to build progressively more interactive visualizations and dashboards. For example, we may want to explore questions such as:

- Which restaurants have the largest number of reviews?
- How are restaurants distributed across cities or regions?
- What types of cuisine are most common?
- How do ratings differ across areas?
- What changes when we filter the data by city, region, or rating?

This is where interactivity becomes important. A static chart can answer one fixed question. An interactive dashboard allows the user to ask many related questions by changing filters, selecting values, and exploring the data directly.

A typical dashboard may include:

- **charts**, such as bar charts, line charts, scatter plots, maps, or pie charts;
- **tables**, for showing detailed records;
- **filters**, such as dropdowns, sliders, checkboxes, or date selectors;
- **summary indicators**, such as counts, averages, totals, or percentages;
- **interactions**, where one user action updates one or more visualizations.

In this lab, we will see how this works in practice. We will start from individual Plotly charts and then use Dash to organize them into a small web application.

The general idea is:

```text
data → visualizations → layout → filters → callbacks → interactive dashboard
```

Plotly helps us create the visualizations. Dash helps us turn these visualizations into an interactive application that runs in the browser.

You can find examples of dashboards and interactive data applications built with Plotly and Dash here:

https://plotly.com/examples/

You do not need to understand these examples in detail now. The purpose of looking at them is to get a sense of what is possible: dashboards can range from simple pages with one chart and one dropdown to complete analytical applications with multiple views, filters, maps, tables, and interactive controls.


## Required Setup

Before the lab, please make sure you have the following installed:

1. **Python 3**  
   Python 3.10 or newer is recommended.

2. **A way to write and run Python files**  
   You may use any code editor or IDE you prefer, such as Visual Studio Code, PyCharm, Spyder, or even a simple text editor together with a terminal.

3. **A browser**  
   Dash applications run locally on your computer and are viewed through the browser.

During the demonstration, we will use Visual Studio Code because it makes it easy to show the code, project files, and terminal in one place. However, it is not required.

## Installing the Required Python Packages

From a terminal, install the required packages:

```bash
pip install dash plotly pandas jupyter
```

## Getting the Datasets

Download and unzip the datasets from:

https://github.com/stavmars/plotly-dash-lab/raw/main/datasets.zip

After extracting the file, make sure that your working folder contains a `datasets/` directory.


## Outline of the Lab

### Part 1: Plotly

- [Introduction to Plotly Notebook](Introduction_to_Plotly.ipynb)

In this part, you will learn how to create interactive charts with Plotly.

Topics include:

- loading data with pandas;
- creating bar charts, line charts, and scatter plots;
- customizing chart titles, axes, and labels;
- using Plotly interactivity such as hover, zoom, and pan.

### Part 2: Introduction to Dash

- [Introduction to Dash](1_Introduction_to_Dash.md)

In this part, you will learn:

- what Dash is;
- how a Dash app is structured;
- how to create a minimal Dash application;
- how to run a Dash app locally.

### Part 3: Dash Components

- [Dash Components](2_Dash_Components.md)

In this part, you will learn how to use:

- `html` components for page structure;
- `dcc.Graph` for embedding Plotly figures;
- basic styling with Python dictionaries.

### Part 4: Dash Callbacks

- [Dash Callbacks](3_Dash_Callbacks.md)

In this part, you will learn how callbacks make a dashboard interactive.

You will add:

- a dropdown for city selection;
- a callback that filters the data;
- a bar chart that updates automatically when the user changes the selected city.

### Part 5: More Advanced Dashboard Example

- [Restaurants in Greece Dashboard: A More Complex Example](4_Advanced_Dash_Example.md)

In this part, you will work with a dashboard that includes:

- region filtering;
- a rating range slider;
- multiple charts;
- multiple callback outputs.



## Additional Resources

- Plotly documentation: https://plotly.com/python/
- Dash documentation: https://dash.plotly.com/
- Dash callbacks: https://dash.plotly.com/basic-callbacks
- Dash components: https://dash.plotly.com/dash-core-components
- Plotly and Dash examples: https://plotly.com/examples/