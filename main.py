import pandas as pd
import numpy as np
import seaborn.objects as so


# from matplotlib import style

def analyze_world_indicators(csv_url):
    # Download World Development Indicators
    wdi = pd.read_csv(csv_url)

    # GDP Per Capita has a REALLY long right tail, so we want to log it for readability.
    wdi["Log GDP Per Capita"] = np.log(wdi["GDP per capita (constant 2010 US$)"])

    # Plot
    my_chart = (
        so.Plot(
            wdi, x="Log GDP Per Capita", y="Mortality rate, under-5 (per 1,000 live births)"
        )
        # .add(so.Line(), so.PolyFit(order=2))
        .add(so.Dot())
        .label(title="Log GDP and Under-5 Mortality")
        # .theme({**style.library["seaborn-whitegrid"]})
    )
    
    my_chart.show()

    return wdi, my_chart

# Example usage
csvurl = "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
data, chart = analyze_world_indicators(csvurl)

# Print some statistical data
print(data.describe())

