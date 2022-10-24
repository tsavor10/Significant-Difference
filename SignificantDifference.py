# import statements
import numpy as np
import pandas as pd
import scipy as sp
from scipy import stats
from pandas_datareader.data import DataReader

# header
print("****************************************")
print("Significant Difference Between Two Stocks")
print("****************************************")
print()

# input statements
start_date = input("Enter Start Date (yyyy-mm-dd): ")
end_date = input("Enter End Date (yyyy-mm-dd): ")
print()
stock1 = input("Enter Ticker for First Stock: ")
stock2 = input("Enter Ticker for Second Stock: ")
print()
sigLevel = input("Enter Significance Level: ")
sigLevel = float(sigLevel)
print()

# create stocks using adjusted close
stock1 = DataReader(stock1, 'yahoo', start_date, end_date)['Adj Close']
stock2 = DataReader(stock2, 'yahoo', start_date, end_date)['Adj Close']

def statistics():
    # mean daily returns
    x = stock1.pct_change().dropna()
    y = stock2.pct_change().dropna()
    # ttest to find pval
    pvalA = stats.ttest_ind(x, y)[1]
    print("Significant Difference in the Mean Daily Returns:")
    print("p-value: " + str('{:.5g}'.format(pvalA)));
    if (pvalA > sigLevel):
        print("Due to the p-value being greater than the given significance level, we fail to reject the null hypothesis.")
    else:
        print("Due to the p-value being less than the given significance level, we can reject the null hypothesis.")
    print()
    # ftest to find pval
    if (np.var(y) > np.var(x)):
        f = np.var(y) / np.var(x)
    else:
        f = np.var(x) / np.var(y)
    print("Significant Difference in their Volatilities:")
    pvalB =  2 * stats.f.sf(f, len(y) - 1, len(x) - 1)
    print("p-value: " + str('{:.5g}'.format(pvalB)))
    if (pvalA > sigLevel):
        print("Due to the p-value being greater than the given significance level, we fail to reject the null hypothesis.")
    else:
        print("Due to the p-value being less than the given significance level, we can reject the null hypothesis.")
    print()
statistics()


