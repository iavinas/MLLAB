import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def local_regression(x0, X, Y, tau):
    # add bias term
    x0 = np.r_[1, x0]
    X = np.c_[np.ones(len(X)), X]
    # fit model: normal equations with kernel
    xw = X.T * radial_kernel(x0, X, tau)
    beta = np.linalg.pinv(xw @ X) @ xw @ Y
    # predict value
    return x0 @ beta

def radial_kernel(x0, X, tau):
    return np.exp(np.sum((X - x0) ** 2, axis=1) / (-2 * tau * tau))


data = pd.read_csv('tips.csv')
bill = data.total_bill
tip = data.tip
tau = 10
ypred = np.array([local_regression(x0, bill, tip, tau) for x0 in bill])
SortIndex = bill.argsort(0)
xsort = bill[SortIndex]
plt.scatter(bill,tip, color='green')
plt.plot(xsort,ypred[SortIndex], color = 'red', linewidth=5)
plt.xlabel('Total bill')
plt.ylabel('Tip')
plt.show();
