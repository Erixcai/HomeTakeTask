################
### Question 2 ####
################


import pandas as pd
import matplotlib.pyplot as plt

# Helper function 1
# To help the main to refined the data from raw
def load_and_filter_data(file_path, query_conditions):
    df = pd.read_csv(file_path)  # Load the dataset from a CSV file
    # Filter/Preprocess the data based on the query conditions
    refined_df = df.query(query_conditions)
    return refined_df

# Helper function 2
# To generate the figure skeleton: x-axis, y-axis, title, data type etc.
def plot_data(refined_df, x_column, y_column, title, xlabel, ylabel):
    # Plotting the data
    # Setting the same as the figure generated by AI in question 1
    plt.figure(figsize=(10, 6), facecolor='white')
    plt.plot(refined_df[x_column], refined_df[y_column], marker='o')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

def main():
    file_path = 'path_to_csv_file.csv'
    query_conditions = ' '  # For example, the year should be in range of 2013 to 2023
    x_column = 'Year'
    y_column = 'Funding Amount (in millions)'
    title = 'Funding Rounds Over Time'
    xlabel = 'Year'
    ylabel = 'Funding Amount (in millions)'
    # Load and filter the data
    refined_data = load_and_filter_data(file_path, query_conditions) 
    # Plot the data
    plot_data(refined_data, x_column, y_column, title, xlabel, ylabel)

if __name__ == '__main__':
    main()
