# -*- coding: utf-8 -*-

"""
TESTS goes here
"""


from main import analyze_world_indicators
import seaborn.objects as so
import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt



def test_analyze_world_indicators():
    # Define the CSV URL for testing
    test_csv_url = "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"



    # Call the function and capture the returned values
    data, chart = analyze_world_indicators(test_csv_url)

    
    


    # Check if data is a DataFrame
    assert isinstance(data, pd.DataFrame), "data should be a pandas DataFrame"

    # Check if chart is a Seaborn plot object
    assert isinstance(chart, so.Plot), "chart should be a Seaborn plot object"

    # Check if the data DataFrame has been modified correctly
    assert "Log GDP Per Capita" in data.columns, "Log GDP Per Capita column missing"

    

# Run the testing function
test_analyze_world_indicators()
