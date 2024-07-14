import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
      # Read data from the web source "epa-sea-level.csv"
    url = 'https://datahub.io/core/sea-level-rise/r/epa-sea-level.csv'
   
    data = pd.read_csv('url')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], color='blue', label='Original Data')

    # Create first line of best fit for the entire dataset
    slope, intercept, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    years_ext = pd.Series(range(1880, 2051))
    sea_level_pred = intercept + slope * years_ext
    plt.plot(years_ext, sea_level_pred, 'r', label='Fitted Line: All Data')

    # Create second line of best fit for data from 2000 onwards
    recent_data = data[data['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    years_recent_ext = pd.Series(range(2000, 2051))
    sea_level_pred_recent = intercept_recent + slope_recent * years_recent_ext
    plt.plot(years_recent_ext, sea_level_pred_recent, 'g', label='Fitted Line: From 2000')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.grid(True)

    # Save plot and return data for testing (optional)
    plt.savefig('sea_level_plot.png')
    plt.show()

    return plt.gca()
