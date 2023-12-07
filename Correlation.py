import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def explore_correlation(data, selected_countries, indicators_of_interest):
    # Filter data for selected countries and indicators
    selected_data = data[
        data['country_name'].isin(selected_countries) & data['country_code'].isin(indicators_of_interest)]

    # Pivot the data to have 'country_name' and 'year' as indices, and 'indicator_name' as columns
    pivot_data = selected_data.pivot(index=['country_name', 'year'], columns='country_code', values='value')

    # Calculate correlation matrix
    correlation_matrix = pivot_data.corr()

    # Replace NaN values with a large negative value
    correlation_matrix = correlation_matrix.fillna(-999)

    # Plot the correlation matrix as a heatmap using Matplotlib
    plt.figure(figsize=(10, 8))


    # Avoid division by zero by checking for an empty matrix
    if not correlation_matrix.empty:
        cax = plt.matshow(correlation_matrix, cmap='coolwarm')
        plt.colorbar(cax)

        # Set axis labels and title
        plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=90)
        plt.yticks(range(len(correlation_matrix.index)), correlation_matrix.index)
        plt.title('Correlation Matrix of Selected Indicators')

        plt.show()
    else:
        print("Correlation matrix is empty.")


# Load your dataset
file_path = r'C:\Users\USER\Documents\WORK\Shiva\co2_emissions_kt_by_country.csv'
world_bank_data = pd.read_csv(file_path)

# Choose countries and indicators of interest
selected_countries = ['United States', 'China', 'India', 'Brazil']
indicators_of_interest = ['value', 'year']

# Explore and visualize the correlation matrix
explore_correlation(world_bank_data, selected_countries, indicators_of_interest)
