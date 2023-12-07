import pandas as pd

def read_and_transform_data(file_path):
    # Read the World Bank format CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Transpose the DataFrame to have years as columns and countries as rows
    df_transposed = df.pivot(index='country_name', columns='year', values='value')

    # Clean the transposed DataFrame (e.g., handle missing values)
    df_transposed_cleaned = df_transposed.dropna()

    return df_transposed_cleaned

# Example usage:
file_path = r'C:\Users\USER\Documents\WORK\Shiva\co2_emissions_kt_by_country.csv'
result_df = read_and_transform_data(file_path)

# Print the resulting DataFrame
print(result_df)
