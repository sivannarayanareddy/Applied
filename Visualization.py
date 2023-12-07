import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset
file_path = r'C:\Users\USER\Documents\WORK\Shiva\co2_emissions_kt_by_country.csv'
world_bank_data = pd.read_csv(file_path)

# Choose countries and indicators of interest
selected_countries = ['United States', 'China', 'India', 'Brazil']

# Filter data for selected countries
selected_data = world_bank_data[world_bank_data['country_name'].isin(selected_countries)]

# Get unique countries from the filtered data
unique_countries = selected_data['country_name'].unique()

# Choose indicators of interest
indicators_of_interest = ['CO2 emissions (kt)', 'Population growth (annual %)', 'Energy use (kg of oil equivalent per capita)']

# Filter data for selected indicators
selected_data = selected_data[selected_data['country_code'].isin(indicators_of_interest)]

# Pivot the data for time series analysis
pivot_data = selected_data.pivot(index=['country_name', 'year'], columns='country_code', values='value')

# Plot time series data
fig, axes = plt.subplots(nrows=len(indicators_of_interest), ncols=1, figsize=(10, 8), sharex=True)

for i, indicator in enumerate(indicators_of_interest):
    axes[i].set_title(f'Time Series: {indicator}')
    for country in unique_countries:
        try:
            country_data = pivot_data.loc[country]
            axes[i].plot(country_data.index.get_level_values('year'), country_data[indicator], label=country)
        except KeyError:
            print(f"Data not available for {country} and {indicator}")

    axes[i].set_ylabel(indicator)
    axes[i].legend()

plt.xlabel('Year')
plt.tight_layout()
plt.show()

# Correlation analysis
correlation_matrix = pivot_data.corr()

# Plot the correlation matrix as a heatmap
plt.figure(figsize=(10, 8))
cax = plt.matshow(correlation_matrix, cmap='coolwarm')
plt.colorbar(cax)

# Set axis labels and title
plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=90)
plt.yticks(range(len(correlation_matrix.index)), correlation_matrix.index)
plt.title('Correlation Matrix of Selected Indicators')

plt.show()
