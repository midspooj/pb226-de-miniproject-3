# National Income and Infant Mortality

## Data Source

The relationship between a country's GDP per capita (a measure of average income per person) and infant mortality (in particular, the share of every 1,000 children born who do not reach their fifth birthday) is analyzed. You can access the data from the following URL: [World Development Indicators 2015 Dataset](https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv).

## Purpose of the Code

The purpose of this code is to analyze World Development Indicators data, specifically focusing on the relationship between income (measured by GDP per capita) and health outcomes (measured by the under-5 mortality rate) across different countries.

## Code Overview

The purpose of this code is to analyze World Development Indicators data, specifically focusing on the relationship between income (measured by GDP per capita) and health outcomes (measured by the under-5 mortality rate) across different countries.

### 1. Import Libraries:

pandas (abbreviated as pd) for data manipulation.  

numpy (abbreviated as np) for numerical operations.  

seaborn.objects (abbreviated as so) for creating statistical visualizations.
 
### 2. Function: analyze_world_indicators(csv_url):

#### Parameters:

csv_url (str): The URL of the CSV file containing World Development Indicators data.

#### Functionality:

Downloads the World Development Indicators data from the provided CSV URL.  

Applies a logarithmic transformation to the "GDP per capita" column for improved readability.   

Generates a scatter plot visualizing the relationship between log GDP per capita and under-5 mortality rate.

#### Returns:

wdi (pd.DataFrame): The DataFrame containing the analyzed data.  

my_chart (so.Plot()): The chart created using seaborn.objects

### 3. Example Usage:

3.1 Demonstrates how to utilize the analyze_world_indicators function by providing a sample CSV URL.  

3.2 Captures the returned DataFrame (data) and plot (chart).  

3.3 Prints summary statistics of the data using data.describe().


## Results

After executing the code, the following descriptive statistics were obtained:

|                     | Log GDP Per Capita |
|---------------------|------------------|
| Count               | 198              |
| Mean                | 8.6996           |
| Std                 | 1.4680           |
| Min                 | 5.4312           |
| 25%                 | 7.5199           |
| 50% (Median)        | 8.7218           |
| 75%                 | 9.7787           |
| Max                 | 12.1520          |

| Mortality Rate (per 1,000 live births) |
|---------------------------------------|
| Count                                 | 193                                   |
| Mean                                  | 31.2964                               |
| Std                                   | 31.4032                               |
| Min                                   | 2.3                                   |
| 25%                                   | 8.0                                   |
| 50% (Median)                          | 17.3                                  |
| 75%                                   | 48.7                                  |
| Max                                   | 135.6                                 |



The summary statistics is made available for all the columns in the csv file.  
Here, the summary statistics offers valuable insights that can be used in correlation analysis, outlier detection, and other potential research directions.  
In outlier detection, for instance, countries with exceptionally high or low values in both variables are identified. These outliers may be interesting for further investigation as they could provide insights into unique economic or health situations.

The visualization below illustrates the relationship between the predictor variable (Log GDP Per Capita) and Infant Mortality Rate.

![image](https://github.com/midspooj/pb226-de-miniproject-2/assets/142264378/f007767e-5b32-48a6-a00e-80b2fca73acd)


## Conclusion

This script helps us understand how a country's economic well-being (measured by log GDP per capita) is related to its infant mortality rate. It also provides basic statistics that are vital for further investigation.

This analysis is important because it sheds light on the potential connection between a nation's wealth and the health of its youngest citizens. It can help identify patterns and disparities, informing policies and interventions aimed at improving infant well-being globally.

