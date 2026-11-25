from fitting_functions import *
import numpy as np
import matplotlib.pyplot as plt
import scipy

data = np.loadtxt("tips.csv", delimiter=",", dtype=str)
bill = data[1:, 0].astype(np.float32)
tip = data[1:, 1].astype(np.float32)

plt.figure()
plt.scatter(bill, tip)
plt.xlabel("Bill ($)")
plt.ylabel("Tip ($)")
plt.title("Bill vs. Tip")
params, params_cov = scipy.optimize.curve_fit(linear, bill, tip)
slope = params[0]
intercept = params[1]

plt.plot(bill, linear(slope, bill, intercept), color="red")

print_equation(slope, intercept, "dollars", "dollars")
plt.show()
# The equation of the line is: y = 0.18221473222560391 dollar/dollar x + -0.2922674195507699 dollars
# Bill vs. Percent Tip

pct_tip = data[1:, 6].astype(np.float32)

plt.figure()
plt.scatter(bill, pct_tip)
plt.xlabel("Bill ($)")
plt.ylabel("Percent Tip (%)")
plt.title("Bill vs. Percent Tip")

params, params_cov = scipy.optimize.curve_fit(linear, bill, pct_tip)
slope = params[0]
intercept = params[1]

plt.plot(bill, linear(slope, bill, intercept), color="red")

print_equation(slope, intercept, "%", "dollars")

plt.show()
# The equation of the line is: y = 0.04881243455874584 %/dollar x + 15.509648238069316 %

# People who order more expensive meals tend to tip a slightly
# higher percentage, but the relationship is weak.

