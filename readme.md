Program that enables time series analysis. It creates a time range plot selected by the user, displaying the time series along with trend line and moving average.

Additional modules used in the project:
- tkinter (console with selection)
- yfinance
- pandas
- matplotlib
- numpy

1. Description:
   - The program fetches data from Yahoo Finance concerning real estate, cryptocurrencies, and commodities prices. Based on the fetched data, it generates charts depicting price trends within a specified time interval.
   
2. Libraries: (exact versions are in the requirements file)
   - tkinter: library for creating GUI,
   - yfinance: library for fetching price data from Yahoo Finance,
   - pandas: library for data analysis,
   - matplotlib: library for creating plots,
   - numpy: library for numerical array operations.
   
3. Graphical Interface:
   - The program features a graphical interface based on the tkinter library.
   - The program window consists of a title and buttons for selecting desired data.

4. Functionality:
   - After selecting the data, the program prompts for the start and end dates of the time interval to view price trends.
   - Subsequently, the program fetches data from Yahoo Finance and generates a chart depicting price changes within the specified time range.
   - The chart includes a moving average and a trend line.

5. Scope of Operation:
   - #real estate from 2013
   - #coal from 2018
   - #oil from 2002
   - #gas from 2002
   - #uranium from 2010
   - #btc from 2015

6. User Instructions:
   - Running the Program:
     - Run the file containing the program code.
   - Selecting Data:
     - Choose the desired data by clicking the appropriate button.
   - Entering Dates:
     - After selecting data, enter the start and end dates of the time interval.
   - Generating the Chart:
     - After entering dates, generate the chart by clicking the "Create Chart" button.

Explanation of Operation:
Functions like "coal", "gas", "oil", "uranium", "real estate", "btc" perform operations on the GUI (remove unnecessary buttons and add new ones [tkinter]). Upon their execution/call, the user is prompted to input the time interval of interest. Just below, there's also a "Create Chart" button generated, which triggers another function upon clicking.

Auxiliary function "commodities" performs operations on the GUI (removing and adding new buttons [tkinter]).

The main functions of the program are:
- "coal_run"
- "gas_run"
- "oil_run"
- "uranium_run"
- "real_estate_run"
- "btc_run"

These functions are associated with the "Create Chart" button. They utilize user-input data along with 'yfinance', using Pandas, Matplotlib, and numpy libraries to perform all necessary calculations for generating the final chart.


 
