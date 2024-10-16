#Andrew Roda
#CSCI 580
#Assignment 3
#10/15/2024
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def main():
    #read csv into x and y values
    df = pd.read_csv('linear_regression_data.csv')
    x_values = df.iloc[:, 0].tolist()
    y_values = df.iloc[:, 1].tolist()
    #setup variables
    n = len(x_values)
    sumxy = 0.0
    sumx = 0.0
    sumy = 0.0
    sumxsq = 0.0
    #get summation used in covariance equation
    for i in range(n):
        sumxy += x_values[i] * y_values[i]
        sumx += x_values[i]
        sumy += y_values[i]
        sumxsq += x_values[i]*x_values[i]
    #get k and b using the equation shown on slide
    k = (n*sumxy-sumx*sumy)/(n*sumxsq-(sumx*sumx))
    b = (sumy - k*sumx)/n
    equation = f"y = {k:.5f}*x+{b:.5f}" #string for legend
    print(k)
    print(n)
    #plot the scatter and the calculated linear model
    plt.scatter(x_values,y_values)
    x = np.linspace(0, 2, 100)
    y = k*x+b
    plt.plot(x,y, label=equation)
    ax = plt.subplot(111)
    ax.legend()
    plt.show()
if __name__ == "__main__":
    main()