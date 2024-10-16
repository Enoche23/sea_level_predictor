import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Load the data from 'epa-sea-level.csv'
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Create a scatter plot using Year (x-axis) and CSIRO Adjusted Sea Level (y-axis)
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data', color='blue')

    # 3. Perform linear regression for the entire dataset (1880 to the latest year)
    slope_all, intercept_all, r_value_all, p_value_all, std_err_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Generate x values for the line of best fit (1880 to 2050)
    years_extended = pd.Series(range(1880, 2051))
    sea_level_pred_all = intercept_all + slope_all * years_extended

    # Plot the first line of best fit (1880 to 2050)
    plt.plot(years_extended, sea_level_pred_all, label='Best Fit (1880-2050)', color='green')

    # 4. Perform linear regression for data from 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

    # Generate x values for the second line of best fit (2000 to 2050)
    years_recent = pd.Series(range(2000, 2051))
    sea_level_pred_recent = intercept_recent + slope_recent * years_recent

    # Plot the second line of best fit (2000 to 2050)
    plt.plot(years_recent, sea_level_pred_recent, label='Best Fit (2000-2050)', color='red')

    # 5. Add labels, title, and legend
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # 6. Save the plot as 'sea_level_plot.png'
    plt.savefig('sea_level_plot.png')

    # 7. Return the plot for testing purposes
    return plt.gca()

