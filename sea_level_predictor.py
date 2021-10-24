import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x, y = df['Year'], df['CSIRO Adjusted Sea Level']

    fig, ax = plt.subplots(figsize=(13,6))
    ax.scatter(x, y)

    # Create first line of best fit
    years = [y for y in range(1880, 2051)]
    res = linregress(x, y)

    x_p1 = pd.Series(years)
    y_p1 = res.slope*x_p1 + res.intercept

    plt.plot(x_p1, y_p1, 'red')

    # Create second line of best fit
    df2 = df[df['Year'] >= 2000]
    
    x_2, y_2 = df2['Year'], df2['CSIRO Adjusted Sea Level']
    res_2 = linregress(x_2, y_2)

    x_p2 = pd.Series(years[120:])
    y_p2 = res_2.slope*x_p2 + res_2.intercept

    plt.plot(x_p2, y_p2, 'yellow')

    # Add labels and title
    ax.set_xlabel('Year', size=13)
    ax.set_ylabel('Sea Level (inches)', size=13)
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()