# Futures-Trading-Tool
## Video Demo: <URL here>


### Introduction

This program will act as an aid for futures traders. As of now, the program allows the user to choose between the E-Mini 
S&P 500 or Moo Moo Inc. When the user inputs their ticker, the program will pull the index data from yfinance, a free API from Yahoo Finance. (Note: The data will be delayed by 15mins. A future effort to incorporate data is likely). By analyzing the data from yfinance, the program will output a strategy for the trader to consider implementing. This program aims to ease the decision making of the trader and allow them to focus on other indicators and strategies to improve their trading odds!

### Files Explained

#### project.py

This is the top file where `main` is found. This file imports several other functions that I wrote. Specifically, it imports: `scraper`, `trends`, and all the functions found in position. The file also imports ta and pandas. Although all the files in `/library` could have been implemented directly in `project.py`, I separated them into libraries to gain experience with modular design and imports.

`project.py` is made up of 7 functions in total. The first function, `main`, is responsible for prompting the user for the specific ticker they want to receive a strategy for and prints out the strategy. When the user inputs their ticker, the second function, `check_ticker`, is called to ensure that the inputted ticker is valid. If not, it will let the user know to input a valid ticker and re-prompt the user. 

With a valid ticker, the program will call the imported `scraper` function and unpack the data from `scraper` into several important variables, one of which is `prices`. The variable `prices` is a list of dictionaries with the closing, high, and low prices from the past 60 days. The program will then show the user the High, Low, and Closing prices for the most recent active day, and the day before that using the third and fourth function native to this file, respectively. In the program, I have it set as today and yesterday prices, but in reality, the market is closed on Saturdays, Sundays, and several holidays. 

The fifth function defined in `project.py` is called `find_trend_and_strategy`. It takes as input "today" and "yesterday" prices as well as the support and resistance points. This function has 2 nested functions within it, both of which are imported to the file. The first function called is the imported `trends` function which returns a message and type. Based on the type of trend, a corresponding function is called and returns another message and type. This corresponding message and type is then unpacked to the variables assigned to the `find_trend_and_strategy` function.

The sixth function defined in `project.py` is the `indicators` function. This function takes as input the prices list. Defined in this function is the equations for all the indicators. So far, I have only implemented 3 indicators into this program: Relative Strength Index, Stochastic Oscillator, Average Directional Movement. With dozens of indicators, these three tend to be some of the most used. There is potential to add more indicators in the future. It should be noted that the code for the ADX indicator calculator
```python
    df = pd.DataFrame(prices) 
    adx_indicator = ADXIndicator(high=df['high'], low=df['low'], close=df['close'], window=14)
    adx = adx_indicator.adx().iloc[-1]  
```
was retrieved using an online source. The actual calculation for the ADX is very complex, so I decided to not increase the complexity of the project and used the `ta` package. The `indicators` function will then return the status of each indicator.

The final function defined in `project.py` is the `final_strategy` function. This function takes as input the type from the `find_trend_and_strategy` function and the status of each indicator. Based on the status and type, the function will print the strategy that user should consider.


#### test_project.py

This file is the test file for `project.py`. Due to the complexity of several of the functions, only the first 3 functions are tested. These are simple functions but are crucial to the project and will ensure the user is viewing the correct data.


#### requirements.txt

This file contains a list of all the `pip`-installable packages.


#### scraper.py

The `scraper.py` file defines the `scraper` function. This function will "scrape" the data received from the `yfinance` package. Using the valid ticker received from the user, the `scraper` function will call the history from the ticker and save that data to a list of dictionaries. The `scraper` function will also calculate the pivot points for that specific ticker. This function returns the prices and pivot points.


#### trends.py

`trends.py` houses the trends function which takes as input the yesterday high and low prices as well as the today high and low prices. Based on those four variables, the trends function returns a `string` describing the kind of trend as well as an `int`. The int is the numeric value of the string. I had this function return both a `string` and `int` in case I wanted to use the message in the future for another function. The main `project.py` only uses the `int` type.

#### position.py

The final file for this project is `position.py` which houses four different functions: `up_day`, `down_day`, `inside_day`, and `outisde_day`. These functions take as input a combination of today's closing prices and pivot points, depending on the kind of day. Depending on the `int` type that is returned by the `trends` function, the main file will call one of the functions defined in `position.py`. This function will return the strategy, or position, that the user should implement. 


### Installation

```bash
pip install -r requirements.txt
python project.py
```

### Usage

```bash
python project.py
```

### Example Output

```Ticker(s): E-mini S&P 500 Futures (ES=F) - Moo Moo (MOO)  
Enter ticker symbol: ES=F

Relative Strength Index: 51.56  
Stochastic: 43.02  
Average Directional Index (ADX): 14.38

Today's Prices - High: 6800.0, Low: 6780.0, Close: 6843.0   
Yesterday's Prices - High: 6872.5, Low: 6806.25, Close: 6823.0

Down Day Strategy:   
Review market conditions for volatility
```

### Testing

```bash
pytest test_project.py
```


