# Data Visualization Tool
This Python script is the answer to Question 2:'if i give you a large chunk of data and a query, can you write a program to generate a chart similarly? using llm and python'.
This Python script is designed to load data from a CSV file, apply filtering based on specific conditions, and plot the results. It is particularly useful for visualizing trends in datasets, such as funding amounts over the years.
Please noticed that, please modify the file_path and query_condition before use it.

## Installation

Before running the script, ensure that Python is installed on your machine along with the following libraries:
- `pandas`
- `matplotlib`

You can install these libraries using pip:

```bash
pip install pandas matplotlib
```
## How to run
Please noticed that, please modify the file_path and query_condition to the correct one before run it.

## How to use
Loading and Filtering Data: The script loads data from a specified CSV file and filters it based on conditions provided in the query_conditions variable.
Data Visualization: After filtering, the data is visualized through a line plot. You can customize the x-axis, y-axis, title, and labels by modifying the parameters in the plot_data function.
