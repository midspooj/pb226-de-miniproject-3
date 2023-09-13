from polars_de import generate_scatter_plot
import polars as pl

def test_generate_scatter_plot():
    # Define the CSV path for testing
    test_csv_path = "path_to_your_test_csv_file.csv"

    # Call the function and capture the returned values
    plot, summary_stats = generate_scatter_plot(test_csv_path)

    # Check if plot is not None
    assert plot is not None, "plot should not be None"

    # Check if summary_stats is a DataFrame
    assert isinstance(summary_stats, pl.DataFrame), "summary_stats should be a polars DataFrame"

    # Check if summary_stats has the expected number of columns
    expected_num_columns = 4  # Assuming there are 4 columns in the summary
    assert len(summary_stats.columns) == expected_num_columns, f"summary_stats should have {expected_num_columns} columns"

    # Check if summary_stats has at least one row
    assert len(summary_stats) >= 1, "summary_stats should have at least one row"

# Run the testing function
test_generate_scatter_plot()
    
    


    # Check if data is a DataFrame
    assert isinstance(data, pd.DataFrame), "data should be a pandas DataFrame"

    # Check if chart is a Seaborn plot object
    assert isinstance(chart, so.Plot), "chart should be a Seaborn plot object"

    # Check if the data DataFrame has been modified correctly
    assert "Log GDP Per Capita" in data.columns, "Log GDP Per Capita column missing"

    

# Run the testing function
test_analyze_world_indicators()
