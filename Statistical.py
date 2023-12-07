import pandas as pd

def explore_statistics(data, countries_of_interest):
    # Select data for the specified countries
    selected_data = data[data['country_name'].isin(countries_of_interest)]

    # Calculate summary statistics using .describe()
    summary_stats = selected_data.groupby('country_name')['value'].describe()

    # Calculate additional statistics: median and standard deviation
    median_stats = selected_data.groupby('country_name')['value'].median()
    std_stats = selected_data.groupby('country_name')['value'].std()

    # Combine all statistics into a single DataFrame
    result_df = pd.concat([summary_stats, median_stats, std_stats], axis=1)

    # Create dynamic column names based on the statistics
    custom_columns = []
    for stat in summary_stats.columns:
        custom_columns.extend([f"{stat} ({country})" for country in summary_stats.index])

    # Slice the result_df columns based on the length of custom_columns
    result_df.columns = custom_columns[:len(result_df.columns)]

    return result_df

# Example usage:
file_path = r'C:\Users\USER\Documents\WORK\Shiva\co2_emissions_kt_by_country.csv'
world_bank_data = pd.read_csv(file_path)

# Specify countries of interest (you can change this list)
selected_countries = ['United States', 'China', 'India', 'Brazil']

# Explore statistics for the selected countries
statistics_result = explore_statistics(world_bank_data, selected_countries)

# Print the resulting DataFrame with summary statistics
print(statistics_result)
